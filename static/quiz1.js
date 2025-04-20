let options = [];
let i = 0;

function feedback(index) {
    $("#quiz1-row").empty();
    
    let facecol = $("<div>");
    $(facecol).addClass("col-3");
    let faceimg = $("<img>");
    faceimg.attr("src", options[index - index%4]["img"]);
    faceimg.addClass("quiz1-face");
    facecol.append(faceimg);

    let col = $("<div>");
    $(col).addClass("col-3");
    let img = $("<img>");
    img.attr("src", options[index]["img"]);
    img.addClass("quiz1-option-clicked");
    col.append(img);

    let feedbackcol = $("<div>");
    $(feedbackcol).addClass("col-3 feedback");
    feedbackcol.text(options[index]["feedback"]);
    if (options[index]["correct"] == 1) feedbackcol.css("color", "green");
    else feedbackcol.css("color", "red");


    let next = $("<button>");
    next.text("Next");
    next.addClass("btn btn-primary");
    next.attr("id", "next-btn");
    feedbackcol.append(next);

    $("#quiz1-row").append(facecol);
    $("#quiz1-row").append(col);
    $("#quiz1-row").append(feedbackcol);

    $("#next-btn").on("click", function() {
        if (i==1) get_question(i);
        if (i==2) window.location.href = "/quiz2";
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
    i++;
    let index = $(this).attr("id");
    feedback(index);
});
