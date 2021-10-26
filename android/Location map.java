 if (googleMap == null) {
        googleMap = ((MapFragment) getFragmentManager().findFragmentById(
                R.id.map)).getMap();

        // check if map is created successfully or not
        if (googleMap == null) {
            Toast.makeText(getApplicationContext(),
                    "Sorry! unable to create maps", Toast.LENGTH_SHORT)
                    .show();
        }
    }
    googleMap.setMyLocationEnabled(true);
    Location myLocation = googleMap.getMyLocation();  //Nullpointer exception.........
    LatLng myLatLng = new LatLng(myLocation.getLatitude(),
            myLocation.getLongitude());

    CameraPosition myPosition = new CameraPosition.Builder()
            .target(myLatLng).zoom(17).bearing(90).tilt(30).build();
    googleMap.animateCamera(
        CameraUpdateFactory.newCameraPosition(myPosition));