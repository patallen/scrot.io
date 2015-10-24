(function(){
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
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
