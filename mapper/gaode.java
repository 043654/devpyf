package cn.iui.autoTest.mapper;

import lombok.extern.slf4j.Slf4j;

/***
 /**
 * @description:
 * @author: DongLee
 */
@Slf4j
public class gaode extends BaseMapper {

    private static final String BASEURL;
    private static final String VERSION = "v3";

    static {
        try {
            BASEURL = new gaode().baseInfo();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public String getTQ() {
        String dd = BASEURL + "\\" + VERSION + "\\" + "weather\\weatherInfo?city=110101&key=5b89efe69c768fe889040bf11f3336b8";
        log.info(dd);
        return dd;
    }

    public static void main(String[] args) {
        new gaode().getTQ();
    }
}
