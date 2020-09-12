//Declare global variables 
let numberOfStations;
let selectedStationId;
let stations = [];

const ttc = document.getElementById('TTC');
const tube = document.getElementById('Tube');
const supertram = document.getElementById('Supertram');


//Select stations/stops data set based on which location was selected 
//TTC event listener
ttc.addEventListener('click', () => {
    //Load stations/stops data files
    stations = []

    numberOfStations = 75; //Remove hard coding of this value
    selectedStationId = randomStation(numberOfStations);
    alert("TTC Station: " + selectedStationId);
}
);
//The tube event listener
//TO DO
//Suoertram event listener
//TO DO

//Randomly select one of the stops/stations within selected data set
const randomStation = numberOfStations => {
    return Math.floor(Math.random() * (numberOfStations + 1));
}


/*
//Load data function using jquery csv
function loadData() {
    var data;
    $.ajax({
        type: "GET",
        url: "./resources/TTC-Stations-csv.csv",
        dataType: "text",
        success: function (response) {
            data = $.csv.toArrays(response);
            generateHtmlTable(data);
        }
    });
}

//Display stationsData
function generateHtmlTable(data) {
    var html = '<table  class="table table-condensed table-hover table-striped">';

    if (typeof (data[0]) === 'undefined') {
        return null;
    } else {
        $.each(data, function (index, row) {
            //bind header
            if (index == 0) {
                html += '<thead>';
                html += '<tr>';
                $.each(row, function (index, colData) {
                    html += '<th>';
                    html += colData;
                    html += '</th>';
                });
                html += '</tr>';
                html += '</thead>';
                html += '<tbody>';
            } else {
                html += '<tr>';
                $.each(row, function (index, colData) {
                    html += '<td>';
                    html += colData;
                    html += '</td>';
                });
                html += '</tr>';
            }
        });
        html += '</tbody>';
        html += '</table>';
        alert(html);
        $('#csv-display').append(html);
    }
}
*/


//Search for nearest pub to this location 


//Display map of the station and nearest pub with directions


//Display images of this pub


//Display WhatPub info (if available)
