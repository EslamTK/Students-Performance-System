$(function () {
    'use strict';
    $.ajax({
        url: 'http://127.0.0.1:8000/dashboard/administrator_years_counts',
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        data: data,
        success: function (data) {
            console.log(data);
            var year = data.result.map(function(result) {
            return result.year;
           });
            var success = data.result.map(function(result) {
            return result.success;
           });
            var fail = data.result.map(function(result) {
            return result.fail;
           });
            console.log('year: ' + year);
            console.log('success: ' + success);
            console.log('fail: ' + fail);
            /////////
            var lineChartData = {
                labels: year,
                datasets: [
                    {
                        label: 'success',
                        backgroundColor: 'rgba(220,220,220,0.2)',
                        borderColor: 'rgba(220,220,220,1)',
                        pointBackgroundColor: 'rgba(220,220,220,1)',
                        pointBorderColor: '#fff',
                        data: success
                    },
                    {
                        label: 'Fail',
                        backgroundColor: 'rgba(151,187,205,0.2)',
                        borderColor: 'rgba(151,187,205,1)',
                        pointBackgroundColor: 'rgba(151,187,205,1)',
                        pointBorderColor: '#fff',
                        data: fail
                    }
                ]
            }


            var ctx = document.getElementById('canvas-1');
            var chart = new Chart(ctx, {
                type: 'line',
                data: lineChartData,
                options: {
                    scales: {
                yAxes: [{
                    display: true,
                    ticks: {
                        beginAtZero: true,
                        stepSize: 0.2,
                        max: 2
                           }
                     }]
                    },
                    responsive: true
                }
            });
            ///////////
        }
    });

    /*var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };

    
    //getting data from hidden input field
    var my_data = document.getElementById("myData").value;
    console.log(my_data);*/

    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
    /*data = JSON.parse(data);
    console.log(data);

    var label_data = [];
    var success = [];
    var fail = [];


    for (var i = 0; i < data.length; i++) {

        label_data.push(data[i].year);
        success.push(data[i].success);
        fail.push(data[i].fail);
    }
*/

});
