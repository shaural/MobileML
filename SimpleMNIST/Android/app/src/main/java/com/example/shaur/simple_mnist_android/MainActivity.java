package com.example.shaur.simple_mnist_android;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
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
        float[] pixelBuf = convertImage();
    }

    private float[] convertImage() {
        Bitmap imageBitmap = BitmapFactory.decodeResource(getResources(),
                imageIDList[imageListIndex]);
        imageBitmap = Bitmap.createScaledBitmap(imageBitmap, 28, 28, true);
        imageView.setImageBitmap(imageBitmap);
        int[] imageAsIntArr = new int[784];
        float[] imageAsFloatArr = new float[784];
        imageBitmap.getPixels(imageAsIntArr, 0,28, 0,0,28,28);
        for (int i = 0; i < 784; i++) {
            imageAsFloatArr[i] = imageAsIntArr[i] / -16777216; // convert to value between 0 and 1
        }
        return imageAsFloatArr;
    }

    public void loadNextImageClick(View view) {
        // roll over after 9, else +1
        imageListIndex = (imageListIndex >= 9) ? 0 : imageListIndex + 1;
        imageView.setImageDrawable(getDrawable(imageIDList[imageListIndex]));
    }
}
