(function(){
    $watchbtn = $('.watch-website-btn')
    $watchbtn.on("click", function(event){
        $this = $(this);
        console.log($this);
        websiteid = $this.closest('.scrot-box').data("website-id");
        event.preventDefault();
        event.stopPropagation();
        $.post("/ajax/watch/", {'website_id': websiteid}, function(data){
            $this.toggleClass('watching');
        });
    })
})();