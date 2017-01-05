/* 
If document is ready, grab the variables in the url pertaining to grades
split them up into and insert them in a list. 
*/
$(document).ready(function () {
    var gradeInd = window.location.href.indexOf("grade"),
        gradeVar = window.location.href.substring(gradeInd),
        gradeListVar = gradeVar.substring(6),
        gradeListVar1 = gradeListVar.split("%2C");

    validate.setGradeList(gradeListVar1);
    validate.gradeAverage();
});

var validate = (function () {
    /* 
    Valid: If true, form is valid.
    grades: Array/List of grades.
    alphaGradeList: Dictionary of Alphabetical Grade and their corresponding
        max value
    alphaGrade: String variable that carries alphabetical Grade
    */
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
                /* If the grade field is not empty, check to see
                if the values are indeed numbers and sit between 0 and 100. If any of these are false, do not validate. */
                var list = $("#grade").val().split(",");
                validate.setGradeList(list);
                for (i in list) {
                    if (list[i] < 0 || list[i] > 100 || isNaN(list[i])) {
                        valid = false;
                        $("#gradeAlert").text("Invalid Grade Value(s)");
                    }
                }
            }
            /* If valid, calculate the average via validate's
            gradeAverage() function and replace the value attribute
            with the alphabetical equivalent and send that to the
            server. Otherwise, do not validate. */
            if (valid) {
                validate.gradeAverage();
                $("#grade").val(validate.getAlphaGrade());
            } else {
                e.preventDefault();
                return valid;
            }
        },
        /* Put a list of grades inside the private variable, grades */
        setGradeList: function (gradeList) {
            grades = gradeList;
        },
        /* Retrieve the list of grades */
        getGradeList: function () {
            return grades;
        },
        /* Calculate the average of the grades. Send the value to 
        the alphabetizeGrade() function. */
        gradeAverage: function () {
            var average = 0,
                grades = validate.getGradeList();

            for (num in grades) {
                average += parseInt(grades[num]);
            }

            average = average / grades.length;
            validate.alphabetizeGrade(average);
        },
        /* Get the alphabetical equivalent based on the parameter,
        avg. */
        alphabetizeGrade: function (avg) {
            for (k in alphaGradeList) {
                if (avg <= k) {
                    alphaGrade = alphaGradeList[k];
                    break;
                }
            }
        },
        /* Return the alphabetical grade to caller */
        getAlphaGrade: function () {
            return alphaGrade;
        }
    };
}());