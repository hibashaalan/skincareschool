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
        // Get current question page
        const currentPage = pages.eq(currentIndex);
    
        // Check if a radio input is selected
        const selected = currentPage.find('input[type=radio]:checked').length > 0;
    
        if (!selected) {
            currentPage.find('.quiz-options').addClass('border border-danger rounded p-2');
            setTimeout(() => {
                currentPage.find('.quiz-options').removeClass('border border-danger');
            }, 2000);
            alert('Please select an option before proceeding.');
            return;
        }
    
        if (currentIndex < pages.length - 1) {
            currentIndex++;
            showPage(currentIndex);
        }
    });

    $('#case-study-quiz').submit(function (e) {
        const currentPage = pages.eq(currentIndex);
        const selected = currentPage.find('input[type=radio]:checked').length > 0;
    
        if (!selected) {
            e.preventDefault(); // Prevent form submission
            alert('Please select an option before submitting.');
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
    
    $(document).on("change", "input[type=radio]", function () {
        const group = $(this).attr("name");
        $(`input[name=${group}]`).closest("label").removeClass("selected");
        $(this).closest("label").addClass("selected");
    });
});