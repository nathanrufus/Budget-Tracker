import React from 'react';

const Access = () => {
  return (
    <div className="mt-[50px] container mx-auto">
      <div className="bg-[#6246E4] px-[40px] py-[40px] mx-auto rounded-[20px] relative max-w-[1000px]"> {/* Adjusted width, centered */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-[20px]">
          <div className="col-span-1">
            <h2 className="font-Allura text-white text-[36px] md:text-[40px] leading-[45px] md:leading-[50px]">
              Sign Up For Free Early Access
            </h2>
            <form action="#">
              <div className="mt-[20px] flex space-x-[20px]">
                <input
                  type="email"
                  name="email"
                  id="email"
                  placeholder="Enter your email"
                  className="font-ABeeZee text-[16px] bg-[#ffffff1a] p-[15px] rounded-[15px] w-full focus-within:outline-none text-white"
                />
                <button
                  type="submit"
                  className="font-Akaya_Kanadaka text-[18px] text-[#624E4] bg-white px-[30px] py-[15px] rounded-[15px]"
                >
                  Send
                </button>
              </div>
            </form>
          </div>
          <div className="col-span-1 relative">
            <img
              src="/assets/svgs/in_touch.svg"
              alt="In Touch"
              className="absolute top-0 right-0 mt-[20px] mr-[20px]"
            />
            <img
              src="/assets/svgs/subscribe_image.svg"
              alt=""
              className="absolute bottom-0 -right-[250px]"
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Access;
