import React from 'react';
import Slider from 'react-slick';
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

function Testimonials() {// Inline PrevArrow Component
const PrevArrow = (props) => {
  const { className, onClick } = props;
  return (
    <div className={`${className} custom-prev-arrow`} onClick={onClick}>
      ←
    </div>
  );
};

// Inline NextArrow Component
const NextArrow = (props) => {
  const { className, onClick } = props;
  return (
    <div className={`${className} custom-next-arrow`} onClick={onClick}>
      →
    </div>
  );
};

const Testimonial = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    prevArrow: <PrevArrow />, 
    nextArrow: <NextArrow />
  };

  return (
    <div className="container mx-auto mt-[40px]">
      <div className="grid grid-cols-3 gap-8">
        <div className="pr-10">
          <h2 className='my-[8px] font-ABeeZee text-[32px] leading-[42px] text-[#2D2D2D]'>What they say?</h2>
          <p className='font-Amatic_SC text-[18px] leading-[28px] text-[#626262]'>When budgets were being cut and the country was deep in the throes.</p>
        </div>

        <div className="col-span-2 h-full">
          <Slider {...settings}>
            {[1, 2, 3].map((item, index) => (
              <div key={index} className="max-w-[400px] mx-auto h-full border border-[#ECECEC] py-[24px] px-[32px] rounded-[20px] cursor-pointer hover:bg-[#FAFAFA] transition-all duration-150">
                <div className="flex justify-between items-center">
                  <div className="flex space-x-[14px]">
                    <div className="w-[50px] h-[50px] bg-gray-300 rounded-full flex items-center justify-center text-white text-xl font-bold">
                      A
                    </div>
                    <div>
                      <h4 className='font-Allura text-[#343333] text-[16px] leading-[22px]'>Adom Shafi</h4>
                      <p className='font-Amatic_SC text-[14px] leading-[22px] text-[#6D6D6D]'>UI/UX Designer</p>
                    </div>
                  </div>
                  <div className="w-[37px] h-[37px] bg-[#F8F4F4] rounded-full flex justify-center items-center">
                    <p className='font-ABeeZee text-[14px] text-[#2D2D2D]'>{item}</p>
                  </div>
                </div>
                <p className='py-[18px] font-Actor text-[#686767] text-[16px] leading-[24px]'>We are happy to hear you had a positive experience at Noren! We value your input and encourage you to let us know more details about your experience with us.</p>
              </div>
            ))}
          </Slider>
        </div>
      </div>
    </div>
  );
};
}

export default Testimonials;




