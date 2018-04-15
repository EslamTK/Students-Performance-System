$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var my_data = document.getElementById("myData").value;

    //formating data to valid json format
    var data = my_data.slice(10,my_data.length,my_data)
    data = data.replace('>','');
    data = data.replace(/'/g,'"');
    data = JSON.parse(data);
    
    var label_data = [];
    var values = [];
    for(var i = 0; i < data.length; i++){
        label_data.push(data[i].review_item__name);
        values.push(data[i].rate__avg);
    }

    var lineChartData = {
        labels: label_data,
        datasets: [
            {
                label: 'Encourage Preparation',
                backgroundColor: 'rgba(33,52,67,0.2)',
                borderColor: 'rgba(33,52,67,1)',
                pointBackgroundColor: 'rgba(33,52,67,1)',
                pointBorderColor: '#fff',
                data: values
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
