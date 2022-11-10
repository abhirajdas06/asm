$(document).ready(function () {
  $("#datatable").DataTable({scrollX: true}),
    $("#datatable-buttons")
      .DataTable({
        scrollX:        false,
        scrollCollapse: false,
        lengthChange: !1,
        buttons: ["copy", "excel", "pdf", "colvis"],
        
      })
      .buttons()
      .container()
      .appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)");
});
