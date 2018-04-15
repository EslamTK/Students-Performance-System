$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 255)
    };
    //getting data from hidden input field
    var my_data = document.getElementById("myData").value;
    console.log(my_data);
    
    //formating data to valid json format
    var data = my_data.slice(10,my_data.length,my_data)
    data = data.replace('>','');
    data = data.replace(/'/g,'"');
    data = JSON.parse(data);
    console.log(data);

    var label_data = [];
    var review_item = new Array(3);
    var values = [];
    for(var i = 0; i < data.length; i++){
        /*if(label_data.indexOf(data[i].year)){
            if(review_item.indexOf(data[i].review_item__name)){
                values[review_item.indexOf(data[i].review_item__name)].push(data[i].rate__avg);
                console.log(data[i].rate__avg);
            }
            else{
                review_item.push(data[i].review_item__name);
                values
            }

        }
        else*/
            label_data.push(data[i].year);        
    }
    var colors = [];
    for(var i  = 0; i < review_item.length; i++){
        colors.push('rgba('+randomScalingFactor+','+randomScalingFactor+','+randomScalingFactor+',1)');
    }
    var datasetss = [];
    for(var i = 0; i < review_item.length; i++){
        datasetss.push({
            label: 'Knowledge',
            backgroundColor: 'rgba(173,220,202,0.2)',
            borderColor: colors[i],
            pointBackgroundColor: colors[i],
            pointBorderColor: '#fff',
            data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
        });
    }

    var lineChartData = {
        labels: label_data,
        datasets: datasetss
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
