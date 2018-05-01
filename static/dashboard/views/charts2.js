window.onload = default_;
$('#year-selector').change(function () {    
        var selectedYear=$( '#year-selector option:selected' ).val();
        //condition to disabe department_list till select year
        if(selectedYear === ''){
            $("#department-selector").val($("#department-selector option:first").val());
			$('#department-selector').attr('disabled', 'disabled');
			default_();
        }else{
            $('#department-selector').attr('disabled', false);
			$('#dTitle').attr('disabled', 'disabled');
        }   
        console.log("Id: "+selectedYear);
        $('#department-selector').change(function () {  
            var selectedDep=$( '#department-selector option:selected' ).val();
            // send selected year and dep to send_request function 
            send_request(selectedYear,selectedDep);
        });
    });

//method that get the selected year and dep and display new data on the chart
function send_request(selectedYear,selectedDep) {
       'use strict';
        console.log("selectedYear: "+selectedYear);
        console.log("selectedDep: "+selectedDep);
        var depId = 'department_id='+selectedDep+'';    
        var cYear = '&year='+selectedYear+'';
        //var edId = '&educator_id='+3+'';
        var baseUrl = 'http://127.0.0.1:8000/dashboard/educator_rating?';
        var aUrl = baseUrl +  depId + cYear ;
        $.ajax({
            url: aUrl,
            dataType: "json",
            type: 'GET',
            contentType: 'application/json',
            success: function (data) {
                console.log(data.result);
                var label_data = [];
                var values = [];
                //collecting data 
                var label_data = [];
                var rates = [];
                for (var i = 0; i < data.result.length; i++) {
                    label_data.push(data.result[i].review_item__name);
                    rates.push(data.result[i].rate__avg);
                }
                //console.log(label_data);
               var barChartData = {
                    labels: label_data,
                    datasets: [
                        {
                            label: 'Rate',
                            backgroundColor: 'rgba(33,52,67,0.2)',
                            borderColor: 'rgba(33,52,67,1)',
                            pointBackgroundColor: 'rgba(33,52,67,1)',
                            pointBorderColor: '#fff',
                            data: rates
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
    }//end sendrequest function 

function default_ () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    //getting data from hidden input field
    var my_data = document.getElementById("myVar").value;
    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
    data = JSON.parse(data);

    //collecting data 
    var label_data = [];
    var rates = [];
    for (var i = 0; i < data.length; i++) {
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
        type: 'bar',
        data: lineChartData,
        options: {
            responsive: true
        }
    });


}