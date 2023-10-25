package cn.iui.autoTest.mapper;

import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.support.PropertiesLoaderUtils;
import java.util.Properties;

/***
 /**
 * @description:
 * @author: DongLee
 */
public abstract class BaseMapper {

    /***
    /**
     * @description:获取接口url
     * @author: DongLee
     */
    public String baseInfo() throws Exception {
        ClassPathResource classPathResource = new ClassPathResource("config.properties");
        Properties config = PropertiesLoaderUtils.loadProperties(classPathResource);
        Object baseurl = config.get("Baseurl");
        return (String) baseurl;
    }
}
