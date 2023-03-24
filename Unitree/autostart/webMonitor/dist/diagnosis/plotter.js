/*
 * plotter.js
 *
 * Markus Schepp
 * 2023.01.10
 *
 *
 * This file contains client-side JavaScript-functions and
 *  classes for a webbased plotter.
 *
 */



var defaultData = '/diagnosis/bms.csv';
// var urlInput = document.getElementById('fetchURL');
var urlInput = defaultData;
// var pollingCheckbox = document.getElementById('enablePolling');
// var pollingInput = document.getElementById('pollingTime');
var pollingInput = 1;
var chart;

function createChart() {
  chart = Highcharts.chart('container', {
    chart: {
      // type: 'spline'
	type: 'scatter',
	zoomType: 'xy'
    },
    title: {
      text: 'BMS data'
    },
    xAxis: {
       title: {
            enabled: true,
            text: 'time'
        },
        startOnTick: true,
        endOnTick: true,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: ''
        }
    },
    accessibility: {
      announceNewData: {
        enabled: true,
        minAnnounceInterval: 500,
        announcementFormatter: function (allSeries, newSeries, newPoint) {
          if (newPoint) {
            return 'New point added. Value: ' + newPoint.y;
          }
          return false;
        }
      }
    },
    data: {
      csvURL: defaultData,
      enablePolling: true,
      dataRefreshRate: parseInt(pollingInput.value, 10),
      endColumn: 3
    }
  });

  if (pollingInput.value < 1 || !pollingInput.value) {
    pollingInput.value = 1;
  }
}

urlInput.value = defaultData;

// We recreate instead of using chart update to make sure the loaded CSV
// and such is completely gone.
// pollingCheckbox.onchange = urlInput.onchange = pollingInput.onchange = createChart;

// Create the chart
createChart();

