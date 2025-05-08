// static/modal.js
(function($) {
    $(document).on('click', '.nav-btn', function() {
      const $btn    = $(this);
      const $modal  = $btn.closest('.modal');
      const nextId  = $btn.data('next');
      const prevId  = $btn.data('prev');
  
      if (nextId) {
        $modal
          .one('hidden.bs.modal', () => $(nextId).modal('show'))
          .modal('hide');
      }
      else if (prevId) {
        $modal
          .one('hidden.bs.modal', () => $(prevId).modal('show'))
          .modal('hide');
      }
    });
  })(jQuery);
  