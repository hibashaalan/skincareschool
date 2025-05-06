$(document).ready(function () {
    let currentIndex = 0;
    const pages = $('.quiz-page');
    const dots = $('.dot');  // Updated selector

    function showPage(index) {
        pages.hide().eq(index).show();
        dots.removeClass('active').eq(index).addClass('active');

        $('#prev-question').toggle(index > 0);
        $('#next-question').toggle(index < pages.length - 1);
        $('#submit-quiz').toggle(index === pages.length - 1);
    }

    $('#next-question').click(function () {
        const currentPage = pages.eq(currentIndex);
        const selected = currentPage.find('input[type=radio]:checked').length > 0;

        if (!selected) {
            // Add temporary red border to unselected options
            currentPage.find('label.option-box').addClass('border border-danger');
            setTimeout(() => {
                currentPage.find('label.option-box').removeClass('border border-danger');
            }, 2000);

            alert('Please select an option before proceeding.');
            return;
        }

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

    $('#case-study-quiz').submit(function (e) {
        const currentPage = pages.eq(currentIndex);
        const selected = currentPage.find('input[type=radio]:checked').length > 0;

        if (!selected) {
            e.preventDefault();
            alert('Please select an option before submitting.');
        }
    });

    $('#show-amira-info').click(function () {
        $('#amira-info-modal').fadeIn();
    });

    $('#close-modal').click(function () {
        $('#amira-info-modal').fadeOut();
    });

    // Highlight selected image
    $(document).on("change", "input[type=radio]", function () {
        const group = $(this).attr("name");
        $(`input[name=${group}]`).closest("label").removeClass("selected");
        $(this).closest("label").addClass("selected");
    });

    showPage(currentIndex); // initialize
});
