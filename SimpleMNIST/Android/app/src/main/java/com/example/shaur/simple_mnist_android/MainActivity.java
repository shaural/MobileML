package com.example.shaur.simple_mnist_android;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import org.tensorflow.contrib.android.TensorFlowInferenceInterface;

public class MainActivity extends AppCompatActivity {

    static {
        System.loadLibrary("tensorflow_inference");
    }
    private static final String MODEL_FILE = "file:///android_asset/optimized_frozen_mnist_model.pb";
    private static final String INPUT_NODE = "x_input";
    private static final String OUTPUT_NODE = "y_actual";
    private static final int[] INPUT_SHAPE = {1, 784};
    private TensorFlowInferenceInterface inferenceInterface;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inferenceInterface = new TensorFlowInferenceInterface();
        inferenceInterface.initializeTensorFlow(getAssets(), MODEL_FILE);
        
    }
}
