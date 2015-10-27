(function(){
   $addToColBtn = $('.collection-add-btn');
   $pickColModal = $('.collections-modal');
   $closeButton = $('.close-modal-btn');
   $addToColBtn.on('click', function(event){
       event.preventDefault();
       event.stopPropagation();

      $pickColModal.css("display", "block");
   });
   $closeButton.on('click', function(event){
       $(this).closest('.collections-modal').css("display", "none");
   });
})();
