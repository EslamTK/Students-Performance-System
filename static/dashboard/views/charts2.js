$(function () {
    'use strict';
    $.ajax({
        url: 'http://127.0.0.1:8000/dashboard/educator_rating',
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        data: data,
        success: function (data) {
            console.log(data.result);
            // transform json array into normal array
            var rate = data.result.map(function(result) {
            return result.rate__avg;
           }); 
           var review = data.result.map(function(result) {
            return result.review_item__name;
           });      
           console.log('rate_avg: ' + rate); 
           console.log('review: ' + review);    
           //////////
           var barChartData = {
                labels: review,
                datasets: [
                    {
                        label: 'Rate',
                        backgroundColor: 'rgba(33,52,67,0.2)',
                        borderColor: 'rgba(33,52,67,1)',
                        pointBackgroundColor: 'rgba(33,52,67,1)',
                        pointBorderColor: '#fff',
                        data: rate
                    }
                ]
            }

            var ctx = document.getElementById('canvas-1');
            var chart = new Chart(ctx, {
                type: 'bar',
                data: barChartData,
                options: {
                    scales: {
                    yAxes: [{
                        display: true,
                        ticks: {
                            beginAtZero: true,
                                        stepSize: 0.3,
                                        max: 5
                               }
                         }]
                        },
                    responsive: true
                }
            });
           //////////
        }
    });

    /*var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var my_data = document.getElementById("myData").value;
*/
    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
   /*
    data = JSON.parse(data);

    var label_data = [];
    var values = [];
    for (var i = 0; i < data.length; i++) {
        label_data.push(data[i].review_item__name);
        values.push(data[i].rate__avg);
    }  */
});
