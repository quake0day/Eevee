package com.example.trackbaidu;



import com.baidu.location.BDLocationListener;
import com.baidu.location.LocationClient;
import com.baidu.location.LocationClientOption;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;
import android.widget.Toast;


public class GPSService extends Service{
	// update interval (msec)
	// update every 5 min
	public int EXTRA_UPDATE_RATE = 5*60*1000;


	
	public LocationClient mLocationClient = null;
	public BDLocationListener myListener = new MyLocationListener();
	
    @Override
    public IBinder onBind(Intent arg0) {
        // TODO Auto-generated method stub
        return null;
    }
    @Override
    public void onCreate() {
        // TODO Auto-generated method stub
        super.onCreate();

        
    }
    
    @Override
    public void onStart(Intent intent, int startId) {
        // TODO Auto-generated method stub
        super.onStart(intent, startId);
        Log.d("LBS:","OnStart");
        Toast.makeText(getApplicationContext(), "LBS Tracking Service Start", Toast.LENGTH_SHORT).show();
        
        // Initial Baidu Map SDK
		mLocationClient = new LocationClient(getApplicationContext());
		mLocationClient.registerLocationListener(myListener);
		setLocationOption();
		// Start it!
		mLocationClient.start();
		
		// Pull a request
		if (mLocationClient != null && mLocationClient.isStarted())
		{
			mLocationClient.requestLocation();
		}
		else
			Log.d("LBS","locClient is null or not started");
    }
    @Override
    public void onDestroy() {
        // TODO Auto-generated method stub
        super.onDestroy();
    }

    
    private void setLocationOption(){
    	LocationClientOption option = new LocationClientOption();
    	// open GPS when service start
    	option.setOpenGps(true);
    	// Set Result Return type default:gcj02
    	option.setCoorType("bd09ll");
    	// Set request span
    	option.setScanSpan(EXTRA_UPDATE_RATE);
    	// Disable 
    	option.disableCache(true);
    	mLocationClient.setLocOption(option);
   
    }
    

}