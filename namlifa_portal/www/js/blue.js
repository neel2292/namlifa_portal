window.signedTerms = false;
$(document).ready(function() {
    loadSignPad2();
});


function dataURLtoFile2(dataurl, filename) {
    try{
        var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
            bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
        while(n--){
            u8arr[n] = bstr.charCodeAt(n);
        }
        return new File([u8arr], filename, {type:mime});
    }catch(error){
        try{
            var blobObject = new Blob([u8arr], {type: 'mime'});
            return "";
        }catch(error){
            return "";
        }
    }
}

function loadSignPad2() {
    setTimeout(() => {
        signPadLoaded = true;
        $("#signatureWidget2").empty();
        $("#signatureWidget2").jSignature().bind('change', function(e){
            var base64_img = $(e.target).jSignature("getData");
            var signFile = dataURLtoFile(base64_img, 'blue_sign.png');
            window.signFile = base64_img;
            window.signedTerms = true;
        });

        $("#resetSignature2").on("click", function(){
            $("#signatureWidget2").jSignature("reset");
        });
    }, 200);
}
