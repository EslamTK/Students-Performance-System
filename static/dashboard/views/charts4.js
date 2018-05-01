//- term_id
alert(57557);
window.onload = default_;
var selectedYear;
$('#year-selector').change(function () {	
        selectedYear=$( '#year-selector option:selected' ).val();
		//condition to disabe department_list till select year
	    if(selectedYear === ''){
			$("#department-selector").val($("#department-selector option:first").val());
            $('#department-selector').attr('disabled', 'disabled');
			default_();
		}else{
			$('#department-selector').attr('disabled', false);
			//$('#yTitle').attr('disabled', 'disabled');
			$('#dTitle').attr('disabled', 'disabled');
		}	
		console.log("Id: "+selectedYear);
		$('#department-selector').change(function () {	
			var selectedDep=$( '#department-selector option:selected' ).val();
			// send selected year and dep to send_request function 
			send_request(selectedYear,selectedDep);
		});
    });

//value onchange radio_button 
$("input:radio[name=options]").change(function(){
	var ter_id= $('input:radio[name=options]:checked').val();
	console.log("here is : "+ter_id );
});


//default value of radio button
var term_id=$("#rb").prop("checked", true).val();
console.log("test_term: "+term_id);

function send_request(selectedYear,selectedDep) {
    'use strict';
    //var depId = $('#idname').val();
	console.log("selectedYear: "+selectedYear);
	console.log("selectedDep: "+selectedDep);
    var depId = 'department_id='+selectedDep+'';
    var yId = '&year='+selectedYear+'';
    var tId = '&term_id='+term_id+'';
    var bUrl = 'http://127.0.0.1:8000/dashboard/administrator_years_counts?';
    var aUrl = bUrl +  depId + yId + tId;
    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
            var label_data = [];
            var success = [];
            var fail = [];


            for (var i = 0; i < data.result.length; i++) {

                label_data.push(data.result[i].year);
                success.push(data.result[i].success);
                fail.push(data.result[i].fail);
                console.log(data.result[i].year);
                console.log(data.result[i].success);
                console.log(data.result[i].fail);
            }
            /////////
            var lineChartData = {
                labels: label_data,
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
                type: 'bar',
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
}
  
function default_() {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };

    //getting data from hidden input field
    var my_data = document.getElementById("myData").value;
    console.log(my_data);
    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
    data = JSON.parse(data);
    console.log(data);

    var label_data = [];
    var success = [];
    var fail = [];


    for (var i = 0; i < data.length; i++) {

        label_data.push(data[i].year);
        success.push(data[i].success);
        fail.push(data[i].fail);
    }

    var lineChartData = {
        labels: label_data,
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
            responsive: true
        }
    });


}