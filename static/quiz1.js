let options = [];
let i = 0;
let answers = {
    id:"0",
    q1:"",
    q2:"",
    score:0,
};

function transitionPage() {
    $("#quiz1-row").empty();
    $("#quiz1-question").empty();
    $("#quiz1-progress").empty();
    let score = $("<div>");
    score.attr("id", "quiz1-score");
    score.text("Your Score: " + answers["score"] + "/2");
    $("#quiz1-row").append(score);


    let retake = $("<button>");
    let retakeArrow = $("<div>");
    retakeArrow.text("←");
    retakeArrow.css("font-size", "60px");
    retake.append(retakeArrow);
    let retakeText =  $("<div>");
    retakeText.text("Retake Multiple Choice Quiz");
    retake.append(retakeArrow);
    retake.append(retakeText);
    retake.addClass("btn btn-primary text-right");
    retake.attr("id", "retake-btn");
    $("#quiz1-row").append(retake);

    let nextQuiz = $("<button>");
    let nextArrow = $("<div>");
    nextArrow.text("→");
    nextArrow.css("font-size", "60px");
    nextQuiz.append(nextArrow);
    let nextText = $("<div>");
    nextText.text("Continue to Case Study");
    nextQuiz.append(nextText);
    nextQuiz.addClass("btn btn-primary text-left");
    nextQuiz.attr("id", "next-btn"); 
    $("#quiz1-row").append(nextQuiz);

    $("#retake-btn").on("click", function() {
        location.reload();
    });

    nextQuiz.on("click", function() {
        window.location.href = "/quiz2";
    });
}

function post_answers() {
    $.ajax({
        type:"POST",
        url:"quiz1_answers",
        dataType:"json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(answers),
        success: function(){  
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}

function feedback(index) {
    $("#quiz1-row").empty();
    
    let facecol = $("<div>");
    $(facecol).addClass("col-3");

    let col = $("<div>");
    $(col).addClass("col-3");
    let img = $("<img>");
    img.attr("src", options[index]["img"]);
    img.addClass("quiz1-option-clicked");
    col.append(img);

    let desc = $("<div>");
    desc.text(options[index]["desc"]);
    col.append(desc);

    let feedbackcol = $("<div>");
    $(feedbackcol).addClass("col-3 feedback");
    feedbackcol.text(options[index]["feedback"]);
    if (options[index]["correct"] == 1) feedbackcol.css("color", "#6aa84f");
    else feedbackcol.css("color", "red");


    let next = $("<button>");
    next.text("Next");
    next.addClass("btn btn-primary");
    next.attr("id", "next");
    if (options[index]["correct"] == 1) next.css("background-color", "#6aa84f");
    else next.css("background-color", "red");
    feedbackcol.append(next);

    $("#quiz1-row").append(facecol);
    $("#quiz1-row").append(col);
    $("#quiz1-row").append(feedbackcol);

    next.on("click", function() {
        if (i==1) get_question(i);
        if (i==2) transitionPage();
    });
}

function display(options, i) {
    $("#quiz1-row").empty();
    $("#quiz1-question").text(options[i*4]["desc"]);

    for (j=0; j<4; j++) {
        let index = i*4 + j
        let col = $("<div>");
        $(col).addClass("col-3");

        let img = $("<img>");
        img.attr("src", options[index]["img"]);
        if (j==0) img.addClass("quiz1-face");
        else {
            img.addClass("quiz1-option");
            img.attr("id", index);
        }
        col.append(img);
        if (j!=0) {
            let desc = $("<div>");
            desc.text(options[index]["desc"]);
            col.append(desc);
        }

        $("#quiz1-row").append(col);
    }

    if (i==0) {
        $("#quiz1-progress-dot2").css("background-color", "#ccc");
        $("#quiz1-progress-text").text("Progress: 1/2");
    } else {
        $("#quiz1-progress-dot2").css("background-color", "#6aa84f");
        $("#quiz1-progress-text").text("Progress: 2/2");
    }
}

function get_question(i) {
    $.ajax({
        type: "GET",
        url: "quiz1_questions",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            options = result["quiz1arr"]
            display(options, i);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });


}
$(document).ready(function(){
    get_question(i);
})

$(document).on("click", ".quiz1-option", function () {
    let index = $(this).attr("id");
    if (options[index]["correct"]) answers["score"] +=1;
    if (i==0) answers["q1"] = index;
    if (i==1) {
        answers["q2"] = index;
        post_answers();
    }
    i++;
    feedback(index);

});
