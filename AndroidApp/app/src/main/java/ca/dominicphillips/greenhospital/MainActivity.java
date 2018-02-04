package ca.dominicphillips.greenhospital;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.ViewParent;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CheckedTextView;
import android.widget.TextView;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {
    String url = "http://10.218.217.112:5000";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        final SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        final CheckBox remuser = (CheckBox) findViewById(R.id.chkRemUsername);
        final CheckBox rempass = (CheckBox) findViewById(R.id.chkRemPassword);
        final TextView txtName = (TextView) findViewById(R.id.txtUsername);
        final TextView txtPass = (TextView) findViewById(R.id.txtPassword);

        remuser.setChecked(prefs.getBoolean("rem_username",true));
        rempass.setChecked(prefs.getBoolean("rem_password",false));

        if (remuser.isChecked())
            txtName.setText(prefs.getString("txt_username", null));
        if (rempass.isChecked())
            txtPass.setText(prefs.getString("txt_password", null));

        final RequestQueue queue = Volley.newRequestQueue(this);
        findViewById(R.id.btnLogin).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferences.Editor editpre = prefs.edit();
                editpre.putBoolean("rem_username",remuser.isChecked());
                editpre.putBoolean("rem_password",rempass.isChecked());
                editpre.putString("txt_username", remuser.isChecked() ? txtName.getText().toString() : "");
                editpre.putString("txt_password", rempass.isChecked() ? txtPass.getText().toString() : "");
                editpre.apply();

                queue.getCache().clear(); // ugly hack
                queue.add(new LoginRequest(txtName.getText().toString(), txtPass.getText().toString()));
            }
        });
    }

    class LoginRequest extends StringRequest {
        LoginRequest(String username, String password) {
            super(Method.GET, url + "/login?username="+username+"&password="+password, new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    System.out.println("Response is: " + response);
                    if (!response.equals("<Bad Login>")) {
                        Intent myIntent = new Intent(MainActivity.this, ProfileActivity.class);
                        myIntent.putExtra("name", response);
                        MainActivity.this.startActivity(myIntent);
                    }
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    System.out.println("That didn't work!");
                }
            });
        }
    }
}
