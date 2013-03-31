package com.example.trackbaidu;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.SystemClock;

public class BootBroadcast extends BroadcastReceiver {

	@Override
	public void onReceive(Context context, Intent mintent) {
		// TODO Auto-generated method stub
		if(Intent.ACTION_BOOT_COMPLETED.equals(mintent.getAction())){
			// After each re-boot
			// We restart our program
			
			//Intent intent = new Intent(context,GPSService.class);
			//context.startService(intent);
			Intent intent = new Intent(context,Alarmreceiver.class);
			intent.setAction("trackbaidu.action");
			PendingIntent sender = PendingIntent.getBroadcast(context, 0, intent, 0);
			long firstime = SystemClock.elapsedRealtime();
			AlarmManager am = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
			
			// check every 20 secs
			am.setRepeating(AlarmManager.ELAPSED_REALTIME_WAKEUP,firstime,20*1000,sender);
			
		}

	}

}
