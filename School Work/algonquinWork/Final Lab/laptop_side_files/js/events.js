// Event Listeners
// If submit button is clicked, validate form
$("input[type='submit']").click(function (e) {
    validate.validateForm(e);
})

/* 
Blur Event: After losing focus, check to see if the value is no longer empty. If true, remove the alert.

Change Event: On change, remove the alert.
*/
$("#fName").blur(function () {
    if ($("#fName").val() !== "") {
        $("#fnameAlert").text("");
    }
})

$("#lName").blur(function () {
    if ($("#lName").val() !== "") {
        $("#lnameAlert").text("");
    }
})

$("#courses").change(function () {
    $("#coursesAlert").text("");
})

$("#workType").change(function () {
    $("#workTypeAlert").text("");
})

$("#grade").blur(function () {
    if ($("#grade").val() !== "") {
        $("#gradeAlert").text("");
    }
})