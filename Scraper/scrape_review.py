#using playwright
from playwright.sync_api import sync_playwright
import pandas as pd
import time


def count_stars(srcs):
    count =0;
    for src in srcs:
        if src=="//img.lazcdn.com/g/tps/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png":
            count+=1
    return count
    


URL=[#'https://www.daraz.com.np/products/aluminium-alloy-metal-adjustable-laptop-stand-for-10-to-17-inches-mackbooklaptopstab-i105711486-s2280473603.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Astand%253Bnid%253A105711486%253Bsrc%253ALazadaMainSrp%253Brn%253Ac4deabf3a8687c12564718997054cd87%253Bregion%253Anp%253Bsku%253A105711486_NP%253Bprice%253A540%253Bclient%253Adesktop%253Bsupplier_id%253A900152409121%253Bbiz_source%253Ah5_external%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A99%253Bitem_id%253A105711486%253Bsku_id%253A2280473603%253Bshop_id%253A47403%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=5.4E%202&priceCompare=skuId%3A2280473603%3Bsource%3Alazada-search-voucher%3Bsn%3Ac4deabf3a8687c12564718997054cd87%3BoriginPrice%3A54000%3BdisplayPrice%3A54000%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767186062829&ratingscore=4.456942003514938&request_id=c4deabf3a8687c12564718997054cd87&review=1138&sale=5013&search=1&source=search&spm=a2a0e.searchlist.list.0&stock=1',
    #  'https://www.daraz.com.np/products/black-leather-classic-martin-boots-for-men-i131507446-s1038454469.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Ashoes%252Bfor%252Bmen%253Bnid%253A131507446%253Bsrc%253ALazadaMainSrp%253Brn%253Ac13b04b478806e15360fccc5f138a1f6%253Bregion%253Anp%253Bsku%253A131507446_NP%253Bprice%253A988%253Bclient%253Adesktop%253Bsupplier_id%253A900155793202%253Bbiz_source%253Ahttps%253A%252F%252Fwww.daraz.com.np%252F%253Bslot%253A2%253Butlog_bucket_id%253A470687%253Basc_category_id%253A4121%253Bitem_id%253A131507446%253Bsku_id%253A1038454469%253Bshop_id%253A75783%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=1&fs_ab=1&fuse_fs=&lang=en&location=Madhesh%20Province&price=988&priceCompare=skuId%3A1038454469%3Bsource%3Alazada-search-voucher%3Bsn%3Ac13b04b478806e15360fccc5f138a1f6%3BoriginPrice%3A98800%3BdisplayPrice%3A98800%3BsinglePromotionId%3A50000033866003%3BsingleToolCode%3AflashSale%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767199070900&ratingscore=4.367647058823529&request_id=c13b04b478806e15360fccc5f138a1f6&review=340&sale=1898&search=1&source=search&spm=a2a0e.searchlist.list.2&stock=1,'
    #  'https://www.daraz.com.np/products/winter-polar-fleece-warm-jacket-for-men-winter-jacket-for-men-mens-winter-dresses-polar-fleece-jackets-i128316237-s1035571765.html?pvid=9e06922e-31a6-4a52-9dac-18259cc650ab&scm=1007.51705.446532.0&spm=a2a0e.tm80335409.just4u.d_128316237',
    #  'https://www.daraz.com.np/products/25w-charger-for-14-pro-max-usb-c-to-lightning-3-pin-i139031369-s1069746089.html?pvid=d3fd9340-abca-4eb6-b889-9ae32b4f098c&search=jfy&scm=1007.51705.413671.0&spm=a2a0e.tm80335409.just4u.d_139031369',
    #  'https://www.daraz.com.np/products/earphone-with-mic-for-android-smartphones-i443216-s26925279.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Aearphone%253Bnid%253A443216%253Bsrc%253ALazadaMainSrp%253Brn%253A060699ab30a8d6056a16d6b9b5ef4d0a%253Bregion%253Anp%253Bsku%253AOT776EL0QTIKCNAFAMZ%253Bprice%253A150%253Bclient%253Adesktop%253Bsupplier_id%253A9703%253Bbiz_source%253Ahttps%253A%252F%252Fwww.daraz.com.np%252F%253Bslot%253A10%253Butlog_bucket_id%253A470687%253Basc_category_id%253A155%253Bitem_id%253A443216%253Bsku_id%253A26925279%253Bshop_id%253A9881%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=1.5E%202&priceCompare=skuId%3A26925279%3Bsource%3Alazada-search-voucher%3Bsn%3A060699ab30a8d6056a16d6b9b5ef4d0a%3BoriginPrice%3A15000%3BdisplayPrice%3A15000%3BsinglePromotionId%3A50000027110002%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767199713657&ratingscore=3.632258064516129&request_id=060699ab30a8d6056a16d6b9b5ef4d0a&review=155&sale=1374&search=1&source=search&spm=a2a0e.searchlist.list.10&stock=1',
    #  'https://www.daraz.com.np/products/mi-redmi-pocophone-85w-charge-30-charger-type-c-cable-turbo-charger-i127353994-s1823625302.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Acharger%253Bnid%253A127353994%253Bsrc%253ALazadaMainSrp%253Brn%253Af726cdc8f5bd63837510d04e66dfe904%253Bregion%253Anp%253Bsku%253A127353994_NP%253Bprice%253A423%253Bclient%253Adesktop%253Bsupplier_id%253A900157473488%253Bbiz_source%253Ah5_external%253Bslot%253A9%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10002875%253Bitem_id%253A127353994%253Bsku_id%253A1823625302%253Bshop_id%253A93276%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=423&priceCompare=skuId%3A1823625302%3Bsource%3Alazada-search-voucher%3Bsn%3Af726cdc8f5bd63837510d04e66dfe904%3BoriginPrice%3A42300%3BdisplayPrice%3A42300%3BsinglePromotionId%3A50000027110002%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767199801844&ratingscore=3.3866666666666667&request_id=f726cdc8f5bd63837510d04e66dfe904&review=75&sale=262&search=1&source=search&spm=a2a0e.searchlist.list.9&stock=1',
    #  'https://www.daraz.com.np/products/bagmati-green-7-plastic-basin-701-i103996629-s1024760690.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Abucket%253Bnid%253A103996629%253Bsrc%253ALazadaMainSrp%253Brn%253A2b8b61aa38e340176da0c359d28c8b93%253Bregion%253Anp%253Bsku%253A103996629_NP%253Bprice%253A32%253Bclient%253Adesktop%253Bsupplier_id%253A1003306%253Bbiz_source%253Ah5_external%253Bslot%253A2%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10000536%253Bitem_id%253A103996629%253Bsku_id%253A1024760690%253Bshop_id%253A13260%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=32&priceCompare=skuId%3A1024760690%3Bsource%3Alazada-search-voucher%3Bsn%3A2b8b61aa38e340176da0c359d28c8b93%3BoriginPrice%3A3200%3BdisplayPrice%3A3200%3BsinglePromotionId%3A50000027110002%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767199840051&ratingscore=3.4780876494023905&request_id=2b8b61aa38e340176da0c359d28c8b93&review=251&sale=1116&search=1&source=search&spm=a2a0e.searchlist.list.2&stock=1',
    #  'https://www.daraz.com.np/products/multicolor-digital-led-sports-watch-i126037789-s1034144436.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Adigital%252Bwatch%253Bnid%253A126037789%253Bsrc%253ALazadaMainSrp%253Brn%253A3d0cf3a18096acfc0719e51b7af28056%253Bregion%253Anp%253Bsku%253A126037789_NP%253Bprice%253A199%253Bclient%253Adesktop%253Bsupplier_id%253A900154824263%253Bbiz_source%253Ah5_external%253Bslot%253A2%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7759%253Bitem_id%253A126037789%253Bsku_id%253A1034144436%253Bshop_id%253A71288%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=199&priceCompare=skuId%3A1034144436%3Bsource%3Alazada-search-voucher%3Bsn%3A3d0cf3a18096acfc0719e51b7af28056%3BoriginPrice%3A19900%3BdisplayPrice%3A19900%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767199917279&ratingscore=3.382978723404255&request_id=3d0cf3a18096acfc0719e51b7af28056&review=94&sale=317&search=1&source=search&spm=a2a0e.searchlist.list.2&stock=1',
'https://www.daraz.com.np/products/blue-ray-cut-glass-using-for-mobile-laptop-tv-men-women-i116927368-s1038233710.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253AEyeglasses%253Bnid%253A116927368%253Bsrc%253ALazadaMainSrp%253Brn%253Af02ebf0b2c0da30266ac2820481ecc7f%253Bregion%253Anp%253Bsku%253A116927368_NP%253Bprice%253A195%253Bclient%253Adesktop%253Bsupplier_id%253A1011033%253Bbiz_source%253Aall_channel%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10001718%253Bitem_id%253A116927368%253Bsku_id%253A1038233710%253Bshop_id%253A20739%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=195&priceCompare=skuId%3A1038233710%3Bsource%3Alazada-search-voucher%3Bsn%3Af02ebf0b2c0da30266ac2820481ecc7f%3BoriginPrice%3A19500%3BdisplayPrice%3A19500%3BsinglePromotionId%3A50000031710005%3BsingleToolCode%3ApromPrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767374221216&ratingscore=4.411320754716981&request_id=f02ebf0b2c0da30266ac2820481ecc7f&review=795&sale=3996&search=1&source=search&spm=a2a0e.searchlist.list.0&stock=1']
def scrape_reviews(url):
    reviews_data=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto(url, timeout=60000)

        #scroll page to end to load content
        for _ in range(1):
            page.mouse.wheel(0, 1000)
            page.wait_for_timeout(500)


        page.wait_for_selector("div.mod-reviews", timeout=60000)
        page_count=1

        
        print(f"Scraping page {page_count}...")
        count_review=page.query_selector("a.pdp-review-summary__link").inner_text().strip()
            #extract number from review and convert to int
        total_reviews=int(''.join(filter(str.isdigit, count_review)))
        total_click_needed=total_reviews/10 + (1 if total_reviews %10 !=0 else 0)
        print(f"Total reviews: {total_reviews}, Total pages to scrape: {total_click_needed}")

        while page_count<=total_click_needed:
            page.wait_for_selector("div.mod-reviews", timeout=60000)
            reviews=page.query_selector_all("div.mod-reviews div.item")
            print(f"Found {len(reviews)} reviews on page {page_count}")
            
            for reviw in reviews:
            
                try:
                    review=reviw.query_selector("div.content").inner_text().strip()
                    star_imgs=reviw.query_selector_all("div.top div.container-star img.star")
                    srcs=[img.get_attribute("src") for img in star_imgs]
                    rating=count_stars(srcs)

                    reviews_data.append({
                    "review": review,
                    "rating": rating
                    })


                except:
                    comment=""

            if len(reviews)<5 or page_count==int(total_click_needed):
                print("Succed")
                return reviews_data
                
            #click next button
            try:
                next_button=page.query_selector("button.current + button")
                if next_button.is_disabled():
                    break
                next_button.click()
                page_count+=1
                time.sleep(2)
            except:
                break

def convert_to_csv(data,path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print("Successfully saved review and rating to csv")
    



if __name__=="__main__":
    i=6
    for url in URL:
        i=i+1
        path=f"../Data/review{i}"
        review=scrape_reviews(url)
        convert_to_csv(review,path)
