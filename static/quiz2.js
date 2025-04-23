$(document).ready(function () {

    let currentIndex = 0;
    const pages = $('.quiz-page');
    const dots = $('#quiz-progress .progress-dot');

    function showPage(index) {
        pages.hide().eq(index).show();
        dots.css('background-color', '#ccc').eq(index).css('background-color', '#2e86de');

        $('#prev-question').toggle(index > 0);
        $('#next-question').toggle(index < pages.length - 1);
        $('#submit-quiz').toggle(index === pages.length - 1);
    }

    $('#next-question').click(function () {
        if (currentIndex < pages.length - 1) {
            currentIndex++;
            showPage(currentIndex);
        }
    });

    $('#prev-question').click(function () {
        if (currentIndex > 0) {
            currentIndex--;
            showPage(currentIndex);
        }
    });

    showPage(currentIndex); // initialize

    $('#show-amira-info').click(function () {
        $('#amira-info-modal').fadeIn();
    });
    
    $('#close-modal').click(function () {
        $('#amira-info-modal').fadeOut();
    });
    
});