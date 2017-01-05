$(document).ready(function () {
    var gradeInd = window.location.href.indexOf("grade"),
        gradeVar = window.location.href.substring(gradeInd),
        gradeListVar = gradeVar.substring(6),
        gradeListVar1 = gradeListVar.split("%2C");

    validate.setGradeList(gradeListVar1);
    validate.gradeAverage();
});

var validate = (function () {
    var valid = true,
        grades = [],
        alphaGradeList = {
            100: "A",
            79: "B",
            69: "C",
            59: "D",
            49: "F"
        },
        alphaGrade = "";

    return {
        validateForm: function (e) {
            valid = true;

            if ($("#fName").val() === "") {
                $("#fnameAlert").text("Required Field");
                valid = false;
            }

            if ($("#lName").val() === "") {
                $("#lnameAlert").text("Required Field");
                valid = false;
            }

            if ($("#courses")[0].selectedIndex === 0) {
                $("#coursesAlert").text("Required Field");
                valid = false;
            }

            if ($("#workType")[0].selectedIndex === 0) {
                $("#workTypeAlert").text("Required Field");
                valid = false;
            }

            if ($("#grade").val() === "") {
                $("#gradeAlert").text("Required Field");
                valid = false;
            } else {
                var list = $("#grade").val().split(",");
                validate.setGradeList(list);
                for (i in list) {
                    if (list[i] < 0 || list[i] > 100 || isNaN(list[i])) {
                        valid = false;
                        $("#gradeAlert").text("Invalid Grade Value(s)");
                    }
                }
            }

            if (valid) {
                validate.gradeAverage();
                $("#grade").val(validate.getAlphaGrade());
            } else {
                e.preventDefault();
                return valid;
            }
        },
        setGradeList: function (gradeList) {
            grades = gradeList;
        },
        getGradeList: function () {
            return grades;
        },
        gradeAverage: function () {
            var average = 0,
                grades = validate.getGradeList();

            for (num in grades) {
                average += parseInt(grades[num]);
            }

            average = average / grades.length;
            validate.alphabetizeGrade(average);
        },
        alphabetizeGrade: function (avg) {
            for (k in alphaGradeList) {
                if (avg <= k) {
                    alphaGrade = alphaGradeList[k];
                    break;
                }
            }
        },
        getAlphaGrade: function () {
            return alphaGrade;
        }
    };
}());