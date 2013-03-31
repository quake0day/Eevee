package com.example.trackbaidu;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.protocol.HTTP;
import org.apache.http.util.EntityUtils;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.util.Log;


import com.baidu.location.BDLocation;
import com.baidu.location.BDLocationListener;
import com.baidu.location.LocationClient;
import com.baidu.location.LocationClientOption;

public class MyLocationListener implements BDLocationListener {
	// Server ip
	public String SERVER_IP_ADDR = "202.120.38.222";
	public String APPNAME = "test";
	public String USERNAME = "test";
 

	@Override
	public void onReceiveLocation(BDLocation location) {
		// TODO Auto-generated method stub
		StringBuffer sbuf = new StringBuffer(256);
		sbuf.append("time:");
		sbuf.append(location.getTime());
		sbuf.append("\n error code:");
		sbuf.append(location.getLocType());
		sbuf.append("\n Latitude:");
		sbuf.append(location.getLatitude());
		sbuf.append("\n Lontitude:");
		sbuf.append(location.getLongitude());
		Log.d("DATA:",sbuf.toString());
		// If loc success code = 61
		if(location.getLocType() == 61){
			postToServer(location);			
		}

	}

	@Override
	public void onReceivePoi(BDLocation arg0) {
		// TODO Auto-generated method stub

	}

	
    private void postToServer(BDLocation location){

    	SharedPreferences SP = PreferenceManager.getDefaultSharedPreferences(SharedValue.getInstance());
    	USERNAME = SP.getString("username", "NA");
    	APPNAME = SP.getString("apptype", "test");
    	SERVER_IP_ADDR = SP.getString("ip", "202.120.38.222");
    	String uriAPI = "http://"+ SERVER_IP_ADDR + ":8080/submit-feeds";
    	
    	// create new http post
    	final HttpPost httpRequest = new HttpPost(uriAPI);
    	
    	final List <NameValuePair> params = new ArrayList<NameValuePair>();
    	DecimalFormat df = new DecimalFormat("###0.0###");
    	params.add(new BasicNameValuePair("user",USERNAME));
    	params.add(new BasicNameValuePair("app",APPNAME));
    	String latitude = df.format(location.getLatitude());
    	params.add(new BasicNameValuePair("latitude",latitude));
    	String longitude = df.format(location.getLongitude());
    	params.add(new BasicNameValuePair("longitude",longitude));
    	
    	new Thread(new Runnable(){

			@Override
			public void run() {
				// TODO Auto-generated method stub
				try{
					httpRequest.setEntity(new UrlEncodedFormEntity(params,HTTP.UTF_8));
					
					String s = "\nparams to string \n"
							+ params.toString()
							+ "\nhttpRequest params \n"
							+ httpRequest.getParams().toString()
							+ "\nhttpRequest \n"
							+ httpRequest.getRequestLine().toString();
					Log.d("LBS",s);
					
					HttpClient httpclient = new DefaultHttpClient();
					
					// fire the post request
					HttpResponse httpResponse = httpclient.execute(httpRequest);
					String response = null;
					
					if(httpResponse.getStatusLine().getStatusCode() == 200){
						response = EntityUtils.toString(httpResponse.getEntity());
						Log.d("LBS",response);
					}
					else
					{
						response = httpResponse.getStatusLine().toString();
						Log.d("LBS","ERROR RESPONSE: "+response);
					}
					
				}catch(Exception e){
					e.printStackTrace();
				}
			}
    		
    	}).start();
    


    }


}
