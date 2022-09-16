$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,

    start: function (e) {
      $("#modal-progress").modal("show");
    },

    stop: function (e) {
      $("#modal-progress").modal("hide");

      /* If your image is uploaded quickly (say on your local machine ) 
         before the fade animation finishes - you can get the situation where 
         the file has uploaded but the progress bar model is still present.  */

      // Ensure hide occurs after the fade animation has completed
      setTimeout(function () {
        $("#modal-progress").modal("hide")
      }, 1000)
    },

    progressall: function (e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({
        "width": strProgress
      });
      $(".progress-bar").text(strProgress);
    },

    done: function (e, data) {
      if (data.result.is_valid) {
        $("#files tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name +
          "</a></td><td>" + data.result.uploaded_at + "</td></tr>"
        )
      }
    }
  });

});