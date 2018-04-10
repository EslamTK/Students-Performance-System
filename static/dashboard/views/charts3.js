$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 10)
    };
    
    var my_data = document.getElementById("myVar").value;
    
    //formating data to valid json format
    var data = my_data.slice(10,my_data.length,my_data)
    data = data.replace('>','');
    data = data.replace(/'/g,'"');
    data = JSON.parse(data);

    //collecting data
    var label_data = [];
    var midpass = [];
    var finalpass = [];
    for(var i = 0; i < data.length; i++){
        
        if(data[i].midterm_pass == 0){
            //for data to be visual remove if valid data entered
            data[i].midterm_pass = randomScalingFactor();
            //for data to be visual remove if valid data entered
            data[i].final_pass = randomScalingFactor();

            label_data.push(data[i].course__name);
            midpass.push(data[i].midterm_pass);
            finalpass.push(data[i].final_pass);
        }     
    }


    var lineChartData = {
        labels: label_data ,
        datasets: [
            {
                label: 'Midterm Pass',
                backgroundColor: 'rgba(220,220,220,0.2)',
                borderColor: 'rgba(220,220,220,1)',
                pointBackgroundColor: 'rgba(220,220,220,1)',
                pointBorderColor: '#fff',
                data: midpass
            },
            {
                label: 'Fail',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                pointBorderColor: '#fff',

                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
            ,
            {
                label: 'Final Pass',
                backgroundColor: 'rgba(234,209,204,0.2)',
                borderColor: 'rgba(234,209,204,1)',
                pointBackgroundColor: 'rgba(234,209,204,1)',

                pointBorderColor: '#fff',
                data: finalpass
            }
            ,
            {
                label: 'Fail',
                backgroundColor: 'rgba(41,54,61,0.2)',
                borderColor: 'rgba(41,54,61,1)',
                pointBackgroundColor: 'rgba(41,54,61,1)',

                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
        ]
    }


    var ctx = document.getElementById('canvas-1');
    var chart = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: {
            responsive: true
        }
    });


});
