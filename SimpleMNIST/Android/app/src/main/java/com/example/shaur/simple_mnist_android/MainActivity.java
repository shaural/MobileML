package com.example.shaur.simple_mnist_android;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import org.tensorflow.contrib.android.TensorFlowInferenceInterface;

public class MainActivity extends AppCompatActivity {

    // init UI elements
    ImageView imageView;
    TextView textView;

    // Vars to communicate with MODEL file
    static {
        System.loadLibrary("tensorflow_inference");
    }
    private static final String MODEL_FILE = "file:///android_asset/optimized_frozen_mnist_model.pb";
    private static final String INPUT_NODE = "x_input";
    private static final String OUTPUT_NODE = "y_actual";
    private static final int[] INPUT_SHAPE = {1, 784};
    private TensorFlowInferenceInterface inferenceInterface;

    private int imageListIndex = 9;
    private final int[] imageIDList = {
            R.drawable.digit0,
            R.drawable.digit1,
            R.drawable.digit2,
            R.drawable.digit3,
            R.drawable.digit4,
            R.drawable.digit5,
            R.drawable.digit6,
            R.drawable.digit7,
            R.drawable.digit8,
            R.drawable.digit9
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // set up UI elements
        imageView = (ImageView) findViewById(R.id.image_view);
        textView = (TextView) findViewById(R.id.text_view);

        // init inference var to use with model
        inferenceInterface = new TensorFlowInferenceInterface();
        inferenceInterface.initializeTensorFlow(getAssets(), MODEL_FILE);
    }

    // BTN on clicks
    public void predictDigitClick(View view) {

    }
    public void loadNextImageClick(View view) {
        // roll over after 9, else +1
        imageListIndex = (imageListIndex >= 9) ? 0 : imageListIndex + 1;
        imageView.setImageDrawable(getDrawable(imageIDList[imageListIndex]));
    }
}
