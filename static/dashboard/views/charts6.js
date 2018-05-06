window.onload = default_;
var selectedDep = "";
var selectedYear = "";
$('#year-selector').change(function () {
    // erase old data from chart when update data 
    if (window.chart !== undefined || window.chart !== null) {
        window.chart.destroy();
    }
    selectedYear = $('#year-selector option:selected').val();
    send_request();
});
$('#department-selector').change(function () {
    selectedDep = $('#department-selector option:selected').val();
    send_request();
});

//method that get the selected year and dep and display new data on the chart
function send_request() {
	   'use strict';
		var depId = 'department_id='+selectedDep+'';	
		var cYear = '&year='+selectedYear+'';
		var baseUrl = request_url+'?';
		var aUrl = baseUrl +  depId + cYear;
	
		$.ajax({
			url: aUrl,
			dataType: "json",
			type: 'GET',
			contentType: 'application/json',
			success: function (data) {
				console.log(data.result);
				var label_data = [];
				var values = [];
				for (var i = 0; i < data.result.length; i++) {
					label_data.push(data.result[i].review_item__name);
					values.push(data.result[i].rate__avg);
				}
				//console.log(label_data);
			   var barChartData = {
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
				window.chart = new Chart(ctx, {
					type: 'bar',
					data: barChartData,
					options: {
						/*scales: {
						yAxes: [{
							display: true,
							ticks: {
								beginAtZero: true,
											stepSize: 0.3,
											max: 5
								   }
							 }]
							},*/
						responsive: true
					}
				});
			   //////////
			}
		});
	}//end sendrequest function 


    
function default_() {
    'use strict';
	var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var my_data = document.getElementById("myData").value;

    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
    data = JSON.parse(data);

    var label_data = [];
    var values = [];
    for (var i = 0; i < data.length; i++) {
        label_data.push(data[i].review_item__name);
        values.push(data[i].rate__avg);
    }

    var barChartData = {
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
    window.chart = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            responsive: true
        }
    });
	}