package com.example.trackbaidu;

import android.app.Application;
import android.content.Context;

public class SharedValue extends Application {
	private String _myState;
	private static SharedValue instance = null;
	public SharedValue() {
		// TODO Auto-generated constructor stub
		instance = this;
		_myState="quake0day";
	}
	public void onCreate(){
		super.onCreate();
		instance = this;
	}
	public static Context getInstance(){
		if(instance == null) instance = new SharedValue();
		return instance;
	}
	
	public String getState(){
		return _myState;
	}
	public void setState(String s){
		_myState = s;
	}

}
