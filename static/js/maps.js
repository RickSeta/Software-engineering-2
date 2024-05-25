let map, startMarker, endMarker, directionsService, directionsRenderer;
let currentField = '';

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -22.9068, lng: -43.1729 }, // Centraliza o mapa no Rio de Janeiro
    zoom: 12
  });

  directionsService = new google.maps.DirectionsService();
  directionsRenderer = new google.maps.DirectionsRenderer();
  directionsRenderer.setMap(map);

  const inputStart = document.getElementById("starting_point");
  const inputEnd = document.getElementById("destination");

  const autocompleteStart = new google.maps.places.Autocomplete(inputStart);
  const autocompleteEnd = new google.maps.places.Autocomplete(inputEnd);

  autocompleteStart.addListener('place_changed', function() {
    const place = autocompleteStart.getPlace();
    if (!place.geometry) {
      alert("No details available for input: '" + place.name + "'");
      return;
    }
    map.setCenter(place.geometry.location);
    placeMarker(place.geometry.location, "start");
  });

  autocompleteEnd.addListener('place_changed', function() {
    const place = autocompleteEnd.getPlace();
    if (!place.geometry) {
      alert("No details available for input: '" + place.name + "'");
      return;
    }
    map.setCenter(place.geometry.location);
    placeMarker(place.geometry.location, "end");
  });

  map.addListener("click", (event) => {
    if (currentField) {
      placeMarker(event.latLng, currentField);
    } else {
      alert("Por favor, clique no ícone de mapa ao lado do campo que deseja definir.");
    }
  });

  document.getElementById("starting_point_map_btn").addEventListener("click", () => {
    currentField = "start";
    alert("Clique no mapa para selecionar o local de partida.");
  });

  document.getElementById("destination_map_btn").addEventListener("click", () => {
    currentField = "end";
    alert("Clique no mapa para selecionar o destino.");
  });
}

function placeMarker(location, type) {
  if (type === "start") {
    if (startMarker) {
      startMarker.setPosition(location);
    } else {
      startMarker = new google.maps.Marker({
        position: location,
        map: map,
        label: "A"
      });
    }
    setLocation("starting_point", location);
  } else if (type === "end") {
    if (endMarker) {
      endMarker.setPosition(location);
    } else {
      endMarker = new google.maps.Marker({
        position: location,
        map: map,
        label: "B"
      });
    }
    setLocation("destination", location);
  }
  if (startMarker && endMarker) {
    calculateAndDisplayRoute();
  }
}

function setLocation(inputId, location) {
  const geocoder = new google.maps.Geocoder();
  geocoder.geocode({ location: location }, (results, status) => {
    if (status === "OK") {
      if (results[0]) {
        document.getElementById(inputId).value = results[0].formatted_address;
        document.getElementById(inputId + "_coords").value = location.lat() + ", " + location.lng();
      } else {
        window.alert("No results found");
      }
    } else {
      window.alert("Geocoder failed due to: " + status);
    }
  });
}

function calculateAndDisplayRoute() {
  directionsService.route(
    {
      origin: startMarker.getPosition(),
      destination: endMarker.getPosition(),
      travelMode: google.maps.TravelMode.DRIVING
    },
    (response, status) => {
      if (status === "OK") {
        directionsRenderer.setDirections(response);
        const distance = response.routes[0].legs[0].distance.text;
        const duration = response.routes[0].legs[0].duration.text;
        document.getElementById("results").innerHTML =
          `<p>Distância: ${distance}</p><p>Tempo de viagem: ${duration}</p>`;
      } else {
        window.alert("Directions request failed due to " + status);
      }
    }
  );
}

document.getElementById('search-ride-form').addEventListener('submit', function(event) {
  event.preventDefault();
  calculateAndDisplayRoute();
});
