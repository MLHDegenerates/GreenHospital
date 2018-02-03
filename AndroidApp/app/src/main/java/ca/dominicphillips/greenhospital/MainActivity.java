package ca.dominicphillips.greenhospital;

import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.ViewParent;
import android.widget.Button;
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
        final RequestQueue queue = Volley.newRequestQueue(this);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().setBackgroundDrawable(new ColorDrawable(Color.parseColor("#12412A")));

        ((Button) findViewById(R.id.btnLogin)).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final TextView mTextView = findViewById(R.id.textinfo);
                queue.add(new LoginRequest(((TextView) findViewById(R.id.txtUsername)).getText().toString(), ((TextView) findViewById(R.id.txtPassword)).getText().toString()));
            }
        });
    }

    class LoginRequest extends StringRequest {
        private final String username, password;

        LoginRequest(String username, String password) {
            super(Method.GET, url + "/login", new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    // Display the first 500 characters of the response string.
                    System.out.println("Response is: " + response);
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    System.out.println("That didn't work!");
                }
            });
            this.username = username;
            this.password = password;
        }

        @Override
        protected Map<String, String> getParams() throws AuthFailureError {
            HashMap<String, String> map = new HashMap<>();
            map.put("username", username);
            map.put("password", password);
            return map;
        }
    }
}
