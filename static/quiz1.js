let options = []

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

    $("#quiz1-row").append(facecol);
    $("#quiz1-row").append(col);
    $("#quiz1-row").append(feedbackcol);
    
    if (options[index]["correct"] == 1) feedbackcol.css("color", "green");
    else feedbackcol.css("color", "red");


}

function display(options, i) {
    $("#quiz1-row").empty();
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

        let desc = $("<div>");
        desc.text(options[index]["desc"]);

        col.append(img);
        col.append(desc);
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
    get_question(0);
})

$(document).on("click", ".quiz1-option", function () {
    let index = $(this).attr("id");
    feedback(index);
});