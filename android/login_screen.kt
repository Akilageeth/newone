package com.example.workforceapp1

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment

/**
 * A simple [Fragment] subclass as the default destination in the navigation.
 */
class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)
        var loginbtn = findViewById<Button>(R.id.login_button)

        loginbtn.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            // start your next activity
            startActivity(intent)
            finish()
        }

    }


}
