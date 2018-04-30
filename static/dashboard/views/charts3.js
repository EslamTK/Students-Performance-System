$(function () {
    'use strict';
    $.ajax({
        url: 'http://127.0.0.1:8000/dashboard/educator_courses_counts',
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        data: data,
        success: function (data) {
            console.log(data.result);
            // transform json array into normal array
            var course_name = data.result.map(function(result) {
            return result.course__name;
           });
            var mt_pass = data.result.map(function(result) {
            return result.midterm_pass;
           });
            var fin_pass = data.result.map(function(result) {
            return result.final_pass;
           });
            var ttl = data.result.map(function(result) {
            return result.total;
           });
            // subtract total - pass 
            var mt_fail = ttl.map(function (ttl, idx) {
              return ttl - mt_pass[idx];
            });
           var fin_fail = ttl.map(function (ttl, idx) {
              return ttl - fin_pass[idx];
            });

            /*console.log('course_name: ' + course_name);
            console.log('midterm_pass: ' + mt_pass);
            console.log('final_pass: ' + fin_pass);
            console.log('total_: ' + ttl);
            console.log('mt_fail: ' + mt_fail);
            console.log('final_fail: ' + fin_fail);*/
/////////////
            var barChartData = {
            labels: course_name,
            datasets: [
                {
                    label: 'Midterm Pass',
                    backgroundColor: 'rgba(220,220,220,0.2)',
                    borderColor: 'rgba(220,220,220,1)',
                    pointBackgroundColor: 'rgba(220,220,220,1)',
                    pointBorderColor: '#fff',
                    data: mt_pass
                },
                {
                    label: 'Midterm Fail',
                    backgroundColor: 'rgba(151,187,205,0.2)',
                    borderColor: 'rgba(151,187,205,1)',
                    pointBackgroundColor: 'rgba(151,187,205,1)',
                    pointBorderColor: '#fff',
                    pointBorderColor: '#fff',

                    data: mt_fail
                }
                ,
                {
                    label: 'Final Pass',
                    backgroundColor: 'rgba(234,209,204,0.2)',
                    borderColor: 'rgba(234,209,204,1)',
                    pointBackgroundColor: 'rgba(234,209,204,1)',

                    pointBorderColor: '#fff',
                    data: fin_pass
                }
                ,
                {
                    label: 'Final Fail',
                    backgroundColor: 'rgba(41,54,61,0.2)',
                    borderColor: 'rgba(41,54,61,1)',
                    pointBackgroundColor: 'rgba(41,54,61,1)',

                    pointBorderColor: '#fff',
                    data: fin_fail
                }
            ]
        }


        var ctx = document.getElementById('canvas-1');
        var chart = new Chart(ctx, {
            type: 'bar',
            data: barChartData,
            options: {
                responsive: true
            }
        });

////////////
        }
        });

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 10)
    };

    var my_data = document.getElementById("myVar").value;

    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');


   /* data = JSON.parse(data);

    console.log(data);
    //collecting data
    var label_data = [];
    var midPass = [];
    var midFail = [];
    var finalPass = [];
    var finalFail = [];

    for (var i = 0; i < data.length; i++) {

        if (data[i].midterm_pass == 0) {
            //for data to be visual remove if valid data entered
            //data[i].midterm_pass = randomScalingFactor();
            //for data to be visual remove if valid data entered
            //data[i].final_pass = randomScalingFactor();

            label_data.push(data[i].course__name);
            midPass.push(data[i].midterm_pass);
            midFail.push(data[i].total - data[i].midterm_pass);
            finalPass.push(data[i].final_pass);
            finalFail.push(data[i].total - data[i].final_pass);
        }
    }*/





});
