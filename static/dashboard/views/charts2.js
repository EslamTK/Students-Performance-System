$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    //getting data from hidden input field
    var my_data = document.getElementById("myVar").value;
    //formating data to valid json format
    var data = my_data.slice(10,my_data.length,my_data)
    data = data.replace('>','');
    data = data.replace(/'/g,'"');
    data = JSON.parse(data);
    
    //collecting data 
    var label_data = [];
    var rates = [];
    for(var i = 0; i < data.length; i++){
        label_data.push(data[i].review_item__name);
        rates.push(data[i].rate__avg);
        
       
    }


    var lineChartData = {
        labels: label_data,
        datasets: [
            {
                label: 'Rate',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                data: rates
            },

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
