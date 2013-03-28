package com.example.trackbaidu;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

public class Alarmreceiver extends BroadcastReceiver {

	@Override
	public void onReceive(Context context, Intent intent) {
		// TODO Auto-generated method stub
		
		if(intent.getAction().equals("trackbaidu.action")){
			Intent i = new Intent();
			i.setClass(context,GPSService.class);
			
			// start service
			context.startService(i);
		}

	}

}
