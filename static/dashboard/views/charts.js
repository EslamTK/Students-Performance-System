window.onload = default_;
var selectedYear;
var flag = 0; //flag to save the state of the term button =>(first or second) in window.term_id before select the year and dep
window.selected_year = null;
$('#year-selector').change(function () {
    // erase old data from chart when update data 
    if (window.chart !== undefined || window.chart !== null) {
        window.chart.destroy();
    }
    selectedYear = $('#year-selector option:selected').val();
    //condition to disabe department_list till select year
    if (selectedYear === '') {
        $("#department-selector").val($("#department-selector option:first").val());
        $('#department-selector').attr('disabled', 'disabled');
        default_();
    }
    console.log("Id: " + selectedYear);
    //------------set year value in global variables 
    if (selectedYear !== null) {
        window.selected_year = selectedYear;
    }
    //-------------if flag=0 that mean button not checked > then return null in its value
    if (flag === 0) {
        send_request(selectedYear, null);
    } else { //---------else flag=1 that mean button checked > then return its value
        send_request(selectedYear, window.term_id);
        flag = 0; //-------- return flag = 0 after execute the function 
    }
});

//function applied on change term 
$("input:radio[name=options]").change(function () {
    // erase old data from chart when update data 
    if (window.chart !== undefined || window.chart !== null) {
        window.chart.destroy();
    }
    var ter_id = $('input[name=options]:checked').val();
    console.log("termId : " + ter_id);
    window.term_id = ter_id; //make ter_id global variable
    flag = 1;
    //------------------check if year & department are selected
    if (window.selected_year === null) {
        // if year & department not selected send request with selected term only.
        send_request(null, ter_id);
    } else { //if year & department are selected send request with selected year, department & term.
        console.log("you select year: " + window.selected_year);
        //send request with values of selected year, department & term.
        send_request(window.selected_year, ter_id);

    }
    //---------------------------------------------
});

var std_id = $('#student_id').val();
console.log("sssss: " + std_id);

//default value of radio button
var term_id = $("#rb").prop("checked", true).val();
console.log("test_term: " + term_id);

function send_request(selectedYear, t_id) {
    'use strict';
    console.log("selectedYear: " + selectedYear);
    var yId = '?year=' + selectedYear + '';
    var stdId = '&student_id=' + std_id + '';
    var tId;
    if (t_id === null) {
        tId = '&term_id=' + term_id + '';
    } else {
        tId = '&term_id=' + t_id + '';
    }
    var bUrl = request_url;
    var aUrl;
    // if year is not selected 
    //make url doesn't contain year value as url parameters
    if (selectedYear === null) {
        aUrl = bUrl + tId;
    } else {
        aUrl = bUrl + yId + tId;
    }
    console.log(aUrl);
    if (typeof std_id === 'undefined') {
        aUrl;
    } else {
        aUrl += stdId;
    }
    console.log("URL: " + aUrl);

    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        success: function (data) {
            var label_data = [];
            var midterm = [];
            var final = [];
            for (var i = 0; i < data.result.length; i++) {
                label_data.push(data.result[i].name);
                midterm.push(data.result[i].midterm);
                final.push(data.result[i].final);

            }
            var lineChartData = {
                labels: label_data,
                datasets: [{
                        label: 'MidTerm',
                        backgroundColor: 'rgba(220,220,220,0.2)',
                        borderColor: 'rgba(220,220,220,1)',
                        pointBackgroundColor: 'rgba(220,220,220,1)',
                        pointBorderColor: '#fff',
                        data: midterm
                    },
                    {
                        label: 'Expected Final Grades',
                        backgroundColor: 'rgba(151,187,205,0.2)',
                        borderColor: 'rgba(151,187,205,1)',
                        pointBackgroundColor: 'rgba(151,187,205,1)',
                        pointBorderColor: '#fff',
                        data: final
                    }
                ]
            }

            var ctx = document.getElementById('canvas-1');
            window.chart = new Chart(ctx, {
                type: 'bar',
                data: lineChartData,
                options: {
                    responsive: true,
                                scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                max: 100
                            }
                        }]
                    }
                }
            });

        }
    });

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 255)
    };
}

function default_() {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };

    //getting data from hidden input field
    var my_data = document.getElementById("myVar").value;

    //transform string into valid json string
    var data = my_data.replace(/'/g, '"');

    //trasnform data into json
    data = JSON.parse(data);
    console.log(data);

    //collecting data
    var label_data = [];
    var midterm = [];
    var prediction = [];
    for (var i = 0; i < data.length; i++) {
        label_data.push(data[i].name);
        midterm.push(data[i].midterm);
        prediction.push(data[i].prediction);

    }
    var lineChartData = {
        labels: label_data,
        datasets: [{
                label: 'MidTerm',
                backgroundColor: 'rgba(220,220,220,0.2)',
                borderColor: 'rgba(220,220,220,1)',
                pointBackgroundColor: 'rgba(220,220,220,1)',
                pointBorderColor: '#fff',
                data: midterm
            },
            {
                label: 'Expected Final Grades',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                data: prediction
            }
        ]
    }


    var ctx = document.getElementById('canvas-1');
    window.chart = new Chart(ctx, {
        type: 'bar',
        data: lineChartData,
        options: {
            responsive: true,
                        scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        max: 100
                    }
                }]
            }
        }
    });


    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var barChartData = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
                backgroundColor: 'rgba(220,220,220,0.5)',
                borderColor: 'rgba(220,220,220,0.8)',
                highlightFill: 'rgba(220,220,220,0.75)',
                highlightStroke: 'rgba(220,220,220,1)',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            },
            {
                backgroundColor: 'rgba(151,187,205,0.5)',
                borderColor: 'rgba(151,187,205,0.8)',
                highlightFill: 'rgba(151,187,205,0.75)',
                highlightStroke: 'rgba(151,187,205,1)',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
        ]
    }
    var ctx = document.getElementById('canvas-2');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            responsive: true
        }
    });


    var doughnutData = {
        labels: [
            'Red',
            'Green',
            'Yellow'
        ],
        datasets: [{
            data: [300, 50, 100],
            backgroundColor: [
                '#FF6384',
                '#36A2EB',
                '#FFCE56'
            ],
            hoverBackgroundColor: [
                '#FF6384',
                '#36A2EB',
                '#FFCE56'
            ]
        }]
    };
    var ctx = document.getElementById('canvas-3');
    var chart = new Chart(ctx, {
        type: 'doughnut',
        data: doughnutData,
        options: {
            responsive: true
        }
    });


    var radarChartData = {
        labels: ['Eating', 'Drinking', 'Sleeping', 'Designing', 'Coding', 'Cycling', 'Running'],
        datasets: [{
                label: 'My First dataset',
                backgroundColor: 'rgba(220,220,220,0.2)',
                borderColor: 'rgba(220,220,220,1)',
                pointBackgroundColor: 'rgba(220,220,220,1)',
                pointBorderColor: '#fff',
                pointHighlightFill: '#fff',
                pointHighlightStroke: 'rgba(220,220,220,1)',
                data: [65, 59, 90, 81, 56, 55, 40]
            },
            {
                label: 'My Second dataset',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                pointHighlightFill: '#fff',
                pointHighlightStroke: 'rgba(151,187,205,1)',
                data: [28, 48, 40, 19, 96, 27, 100]
            }
        ]
    };
    var ctx = document.getElementById('canvas-4');
    var chart = new Chart(ctx, {
        type: 'radar',
        data: radarChartData,
        options: {
            responsive: true
        }
    });


    var pieData = {
        labels: [
            'Red',
            'Green',
            'Yellow'
        ],
        datasets: [{
            data: [300, 50, 100],
            backgroundColor: [
                '#FF6384',
                '#36A2EB',
                '#FFCE56'
            ],
            hoverBackgroundColor: [
                '#FF6384',
                '#36A2EB',
                '#FFCE56'
            ]
        }]
    };
    var ctx = document.getElementById('canvas-5');
    var chart = new Chart(ctx, {
        type: 'pie',
        data: pieData,
        options: {
            responsive: true
        }
    });


    var polarData = {
        datasets: [{
            data: [
                11,
                16,
                7,
                3,
                14
            ],
            backgroundColor: [
                '#FF6384',
                '#4BC0C0',
                '#FFCE56',
                '#E7E9ED',
                '#36A2EB'
            ],
            label: 'My dataset' // for legend
        }],
        labels: [
            'Red',
            'Green',
            'Yellow',
            'Grey',
            'Blue'
        ]
    };


}