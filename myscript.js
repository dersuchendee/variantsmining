var colors = Highcharts.getOptions().colors;
Highcharts.chart('container', {

  chart: {
    type: 'streamgraph',
    marginBottom: 30,
    zoomType: 'x'
  },

  // Make sure connected countries have similar colors
  colors: [
    colors[0],
    colors[1],
    colors[2],
    colors[3],
    colors[4],
    // East Germany, West Germany and Germany
    Highcharts.color(colors[5]).brighten(0.2).get(),
    Highcharts.color(colors[5]).brighten(0.1).get(),

    colors[5],
    colors[6],
    colors[7],
    colors[8],
    colors[9],
    colors[0],
    colors[1],
    colors[3],
    // Soviet Union, Russia
    Highcharts.color(colors[2]).brighten(-0.1).get(),
    Highcharts.color(colors[2]).brighten(-0.2).get(),
    Highcharts.color(colors[2]).brighten(-0.3).get()
  ],

  title: {
    floating: true,
    align: 'left',
    text: 'Variants mining: Fermo e Lucia'
  },
  subtitle: {
    floating: true,
    align: 'left',
    y: 30,
    text: 'Source: Variants mining'
  },

  xAxis: {
    maxPadding: 0,
    type: 'category',
    crosshair: true,
    categories: [
      'Chapter I',
      'Chapter II',
      'Chapter III',
      'Chapter VI',
      'Chapter V',
      'Chapter VI',
      'Chapter VII',
      'Chapter VIII'

    ],
    labels: {
      align: 'left',
      reserveSpace: false,
      rotation: 270
    },
    lineWidth: 0,
    margin: 20,
    tickWidth: 0
  },

  yAxis: {
    visible: false,
    startOnTick: false,
    endOnTick: false
  },

  legend: {
    enabled: false
  },



  plotOptions: {
    series: {
      label: {
        minFontSize: 5,
        maxFontSize: 15,
        style: {
          color: 'rgba(255,255,255,0.75)'
        }
      }
    }
  },

  // Data parsed with olympic-medals.node.js
  series: [{
    name: "IC 1",
    data: [
      253, 188, 178, 199, 220, 180, 250, 315
    ]
  }, {
    name: "IC 3",
    data: [
      10, 13, 4, 10, 10, 5, 8, 22
    ]
  }, {
    name: "IC 4",
    data: [
      0, 1, 0, 0, 0, 1, 1, 0
    ]
  }, {
    name: "IC 5",
    data: [
      1, 1, 0, 0, 0, 0, 0, 0
    ]
  }, {
    name: "IC 6",
    data: [
      0, 0, 0, 1, 0, 0, 0, 0
    ]
  }, {
    name: "IC 7",
    data: [
      0, 0, 1, 0, 1, 1, 0, 0
    ]
  }, {
    name: "IC 8",
    data: [
    0, 0, 0, 0, 0, 1, 0, 0
    ]
  }, {
    name: "INS 1",
    data: [
      17, 10, 13, 11, 8, 7, 17, 17
    ]
  }, {
    name: "LC 1",
    data: [
    177, 117, 114, 145, 145, 118, 199, 233
    ]
  }, {
    name: "LC 2",
    data: [
      19, 13, 21, 24, 26, 15, 30, 35
    ]
  }, {
    name: "LC 3",
    data: [
      32, 20, 11, 18, 22, 13, 27, 35
    ]
  }, {
    name: "LC 4",
    data: [
      3, 3, 3, 2, 2, 4, 4, 12
    ]
  }, {
    name: "LC 5",
    data: [
      2, 1, 1, 0, 0, 0, 1, 0
    ]
  }, {
    name: "LC 6",
    data: [
      0, 0, 1, 0, 1, 0, 0, 0
    ]
  }],

  exporting: {
    sourceWidth: 800,
    sourceHeight: 600
  }

});
