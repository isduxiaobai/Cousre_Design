package com.example.weibobeike;
//适配器文件

import java.util.ArrayList;

import android.content.Context;
import android.graphics.Color;
import android.renderscript.Type;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class myAdapter extends BaseAdapter {
    // 一条微博数据
    private final ArrayList<DataModel> list;
    private final Context context;
    public myAdapter(ArrayList<DataModel> list,Context context){
        super();
        this.list = list;
        this.context = context;
    }

    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return list.size();
    }

    @Override
    public Object getItem(int position) {
        // TODO Auto-generated method stub
        return list.get(position);
    }

    @Override
    public long getItemId(int position) {
        // TODO Auto-generated method stub
        return position;
    }

    static class ViewHolder{
        ImageView iv_icon ;
        ImageView iv_isVip ;
        ImageView iv_picture ;

        TextView tv_username ;
        TextView tv_content ;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder hodler;
        if (convertView == null) {
            convertView = View.inflate(context, R.layout.item, null);
            System.out.println("converview: "+position);
            hodler = new ViewHolder();
            hodler.iv_icon = (ImageView) convertView.findViewById(R.id.iv_icon);
            hodler.iv_isVip = (ImageView) convertView.findViewById(R.id.iv_isVip);
            hodler.iv_picture = (ImageView) convertView.findViewById(R.id.iv_picture);

            hodler.tv_username = (TextView) convertView.findViewById(R.id.tv_username);
            hodler.tv_content = (TextView) convertView.findViewById(R.id.tv_content);


            convertView.setTag(hodler);
        }else {
            hodler = (ViewHolder) convertView.getTag();
        }

        // 取出对应位置的数据模型
        DataModel model = list.get(position);

//		ImageView iv_icon = (ImageView) v.findViewById(R.id.iv_icon);
//		ImageView iv_isVip = (ImageView) v.findViewById(R.id.iv_isVip);
//		ImageView iv_picture = (ImageView) v.findViewById(R.id.iv_picture);
//
//		TextView tv_username = (TextView) v.findViewById(R.id.tv_username);
//		TextView tv_content = (TextView) v.findViewById(R.id.tv_content);

        // 将数据模型显示到控件上
        // 设置头像
        hodler.iv_icon.setImageResource(model.getIcon());

        if (model.isVip()) {  //TRUE 显示VIP
            hodler.iv_isVip.setVisibility(View.VISIBLE);
        }else {
            hodler.iv_isVip.setVisibility(View.GONE);
            hodler.tv_username.setTextColor(Color.parseColor("black"));
        }

        if (model.getPicture() != 0) { //有配图
            hodler.iv_picture.setVisibility(View.VISIBLE);
            hodler.iv_picture.setImageResource(model.getPicture());
        }else {
            hodler.iv_picture.setVisibility(View.GONE);
        }

        hodler.tv_username.setText(model.getUserName());
        hodler.tv_content.setText(model.getContent());

        return convertView;
    }

}
