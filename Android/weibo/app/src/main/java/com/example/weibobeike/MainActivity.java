package com.example.weibobeike;
import java.util.ArrayList;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;
import android.widget.Toast;

public class MainActivity extends Activity {

    //微博内容
    private final String[] content = new String[] {
            "妈妈说，女人一定要爱自己的脸，别人打你左脸，你再把右脸伸过去让他打，不然粉底不一样厚。",
            "奥利奥原味",
            "历经磨难，青蛙王子终于跳上餐桌，希望公主能给他一个吻。公主一见到他，满心欢喜，吧唧着嘴说：「哇塞，好肥的" +
                    "田鸡啊！」","" +
            "号外，号外：大师兄不慎下凡，被数人围观",
            "看到有纸糊的苹果手机。就问:啊哈，这里还有苹果5S啊?老祖宗会用吗?老 板白了我一眼说:乔布斯都亲自下去教了，" +
                    "你还操什么心。我买了一个刚转身要走，老板提醒: 再买个手机套吧!下面蛮潮湿的。我说好，接着老板又" +
                    "说再买个蓝牙耳机吧，最近下面出了 新交规，开车接电话查的严。我又买个蓝牙耳机，老板继续善意提醒" +
                    ":最重要的还要买充电器 啊!回头你祖宗找你要就不好了，光找你要是小事，让你送过去就麻烦了。我又买" +
                    "个充电器， 然后和老板要名片。老板问:要我名片干嘛?我说烧给祖宗啊!万一出了质量问题我好让我祖 宗来找你。",
            "完全豁出去的广告"};

    // 微博头像
    private final int[] icon = new int[] { R.drawable.a50, R.drawable.a7735164184,
            R.drawable.a1, R.drawable.a1516159990, R.drawable.a238221586,
            R.drawable.a424324
    };
    // 微博昵称
    private final String[] userName = new String[] { "笑多了会怀孕", "内涵段子", "西门抽血",
            "西门抽筋", "菠萝吹雪", "果宝特工" };
    // 是否是VIP
    private final boolean[] isVip = new boolean[] { true, true, true, false, false,
            true };

    // 微博配图
    private final int[] picture = new int[] { 0, R.drawable.a926680527,
            R.drawable.a4934348604, 0, R.drawable.a6289891986,
            R.drawable.a603564546
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // 1.找到listview
        ListView lv_list = (ListView) findViewById(R.id.lv_list);
        // 创建可变数组记录 数据模型
        ArrayList<DataModel> list = new ArrayList<DataModel>();
        //2.加载数据
        for (int i = 0; i < userName.length; i++) {
            DataModel model = new DataModel(content[i], icon[i], userName[i], isVip[i], picture[i]);
            list.add(model);
        }

        // 创建数据适配器
        myAdapter adapter = new myAdapter(list,MainActivity.this);
        //3.设置数据适配器
        lv_list.setAdapter(adapter);
        //当选中某一个item时 提示信息
        lv_list.setOnItemClickListener(new myListener());
    }
    public class myListener implements OnItemClickListener{

        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position,
                                long id) {
            // TODO Auto-generated method stub
            DataModel object = (DataModel) parent.getItemAtPosition(position);

            Toast.makeText(getApplicationContext(), object.getUserName(), 0).show();
        }

    }

}
