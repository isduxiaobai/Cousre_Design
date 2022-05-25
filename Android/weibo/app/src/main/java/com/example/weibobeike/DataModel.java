package com.example.weibobeike;
//数据模型文件

public class DataModel {
    // 微博内容
    private String content;
    // 微博头像
    private int icon;
    // 微博昵称
    private String userName;
    // 是否是VIP
    private boolean isVip;
    // 微博配图
    private int picture;

    // 构造方法
    public DataModel(String content, int icon, String userName, boolean isVip,
                     int picture) {
        super();
        this.content = content;
        this.icon = icon;
        this.userName = userName;
        this.isVip = isVip;
        this.picture = picture;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public int getIcon() {
        return icon;
    }

    public void setIcon(int icon) {
        this.icon = icon;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public boolean isVip() {
        return isVip;
    }

    public void setVip(boolean isVip) {
        this.isVip = isVip;
    }

    public int getPicture() {
        return picture;
    }

    public void setPicture(int picture) {
        this.picture = picture;
    }

    @Override
    public String toString() {
        return "DataModel [content=" + content + ", icon=" + icon
                + ", userName=" + userName + ", isVip=" + isVip + ", picture="
                + picture + "]";
    }


}
