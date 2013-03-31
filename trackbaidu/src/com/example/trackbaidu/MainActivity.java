package com.example.trackbaidu;

import com.baidu.location.BDLocationListener;

import com.baidu.location.LocationClient;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.Button;

public class MainActivity extends Activity {
	

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		Button myButton1 = (Button) findViewById(R.id.button1);
		final Activity main_activity = this;
		myButton1.setOnClickListener(new Button.OnClickListener(){
			public void onClick(View v){
				startActivity(new Intent(main_activity, AppPreferences.class));
			}
		});
		
		startService(new Intent(this, GPSService.class));

	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	



}
