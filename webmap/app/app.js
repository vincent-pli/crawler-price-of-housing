'use strict';

require("./app.css");
require("./overview/overview.js");
var angular = require("../node_modules/angular/angular.min.js");


// Declare app level module which depends on views, and components
angular.module('houseApp', [
  'ngRoute',
  'houseApp.overview'
]).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider.otherwise({redirectTo: '/overview'});
}]);
