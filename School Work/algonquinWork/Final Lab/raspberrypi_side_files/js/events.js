$("input[type='submit']").click(function (e) {
    validate.validateForm(e);
})

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