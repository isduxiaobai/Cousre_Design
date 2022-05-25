package com.example.qqlogin;

import android.app.Activity;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.WindowManager;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.Toast;
public class MainActivity extends Activity implements OnClickListener {
    private EditText et_qq_number;
    private EditText et_qq_psw;
    private CheckBox cb_checked;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_HIDDEN);

        Button btn_login = (Button) findViewById(R.id.btn_login);
        et_qq_number = (EditText) findViewById(R.id.et_qq_number);
        et_qq_psw = (EditText) findViewById(R.id.et_qq_psw);
        cb_checked = (CheckBox)findViewById(R.id.cb_checked);
        LinearLayout root = (LinearLayout)findViewById(R.id.root);

        SharedPreferences preferences = getSharedPreferences("config", MODE_PRIVATE);

        String qq_number = preferences.getString("qq_number", "");
        String qq_psw = preferences.getString("qq_psw", "");
        boolean checked = preferences.getBoolean("checked", false);

        if (!(qq_number.isEmpty() || qq_psw.isEmpty())) {
            et_qq_number.setText(qq_number);
            et_qq_psw.setText(qq_psw);
        }

        cb_checked.setChecked(checked);

        //1.实现按钮的监听
        btn_login.setOnClickListener(this);
        //给布局添加监听事件，点击空表退出键盘
        root.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                //退出键盘
                InputMethodManager imm = (InputMethodManager)getSystemService(INPUT_METHOD_SERVICE);
                imm.hideSoftInputFromWindow(v.getWindowToken(), 0);
            }
        });

    }
    // 监听按钮的点击方法
    @Override
    public void onClick(View v) {
        // TODO Auto-generated method stub12
        // 退出键盘
        InputMethodManager imm = (InputMethodManager)getSystemService(INPUT_METHOD_SERVICE);
        imm.hideSoftInputFromWindow(v.getWindowToken(), 0);
        // 2.拿到QQ号和密码
        String qq_number = et_qq_number.getText().toString().trim();
        String qq_psw = et_qq_psw.getText().toString().trim();

        System.out.println(qq_number + " ----" + qq_psw);
        // 3. 判断QQ号和密码是否为空
        if (TextUtils.isEmpty(qq_number) || TextUtils.isEmpty(qq_psw)) {
            // 提示用户
            Toast.makeText(getApplicationContext(), "QQ号码和密码不能为空，请输入",
                    Toast.LENGTH_SHORT).show();
            return;
        }
        // 4. 判断QQ号和密码是否争取 123456 123
        if (qq_number.equals("123456") && qq_psw.equals("123")) {// 正确
            Toast.makeText(getApplicationContext(), "登录成功", Toast.LENGTH_SHORT)
                    .show();
            //5.先判断checkBox是否被选中
            //5.1取checkBox的值
            boolean checked = cb_checked.isChecked();
            //5.2 根据checked的值判断是否存储QQ号和密码
            if (checked) {  //TRUE
                //获取偏好设置
                SharedPreferences sharedPreferences = getSharedPreferences("config", MODE_PRIVATE);
                //获取编辑器
                Editor editor = sharedPreferences.edit();
                //存储数据
                editor.putString("qq_number", qq_number);
                System.out.println("qq_number:"+ qq_number);
                editor.putString("qq_psw", qq_psw);
                System.out.println("qq_number:"+qq_number);
                editor.putBoolean("checked", checked);
                //提交
                editor.commit();
            }else {  //FALSE
                //获取偏好设置
                SharedPreferences sharedPreferences = getSharedPreferences("config", MODE_PRIVATE);
                //获取编辑器
                Editor editor = sharedPreferences.edit();
                //清除数据
                editor.putString("qq_number", "");
                editor.putString("qq_psw", "");
                editor.clear();
                //提交
                editor.commit();
            }

        } else {
            Toast.makeText(getApplicationContext(), "QQ账号或QQ密码错误",
                    Toast.LENGTH_SHORT).show();
        }

    }

}
