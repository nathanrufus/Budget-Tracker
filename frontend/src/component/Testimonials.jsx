import Slider from "react-slick";
import { FaAngleRight, FaAngleLeft } from "react-icons/fa";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

const Testimonial = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 2,
    slidesToScroll: 1,
  };

  const testimonials = [
    { content: "This is the best service ever!", author: "John Doe" },
    { content: "I am so happy with their work!", author: "Jane Smith" },
  ];

  const PrevArrow = ({ onClick }) => (
    <div
      className="h-[48px] w-[48px] border border-[#EDEDED] rounded-full flex justify-center items-center absolute -right-14 top-20 cursor-pointer"
      onClick={onClick}
    >
      <FaAngleLeft size={20} />
    </div>
  );

  const NextArrow = ({ onClick }) => (
    <div
      className="h-[48px] w-[48px] border border-[#EDEDED] rounded-full flex justify-center items-center absolute -right-14 bottom-20 cursor-pointer"
      onClick={onClick}
    >
      <FaAngleRight size={20} />
    </div>
  );

  return (
    <div className="container mx-auto mt-[160px]">
      <h2 className="font-Allura text-[60px] text-[#343333] text-center">Testimonials</h2>
      <Slider {...settings} prevArrow={<PrevArrow />} nextArrow={<NextArrow />}>
        {testimonials.map((testimonial, index) => (
          <div key={index} className="px-5">
            <p className="font-Amatic_SC text-[20px] leading-[30px] text-[#838383] text-center">
              "{testimonial.content}"
            </p>
            <h4 className="font-Allura text-[34px] text-[#2D2D2D] text-center mt-4">
              - {testimonial.author}
            </h4>
          </div>
        ))}
      </Slider>
    </div>
  );
};

export default Testimonial;
