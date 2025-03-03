import React from 'react';

const Contact = () => {
  return (
    <div className="relative">
      
      

      <div className="container mx-auto px-[80px] mt-[100px] pb-20">
        <div className="w-full grid grid-cols-10 gap-x-10">
       
          <div className="col-span-4 mt-[120px]">
            <h2 className="w-[190px] font-Allura text-[42px] leading-[52px] text-[#2D2D2D]">
              Get In Touch With Us
            </h2>
            <p className="mt-[14px] text-[#4F4F4F] font-Amatic_SC text-[16px] leading-[16px]">
              Do you have any questions?
            </p>
          </div>

      
          <div className="col-span-6 relative">
            <form
              action="#"
              className="absolute w-full bg-white p-10 shadow-2xl rounded space-y-[20px] max-w-[800px] mx-auto"
            >

              <div className="flex flex-col">
                <label
                  htmlFor="name"
                  className="font-Akaya_Kanadaka text-[18px] text-[#4F4F4F]"
                >
                  Name
                </label>
                <input
                  type="text"
                  name="name"
                  id="name"
                  className="border-b-[2px] border-[#D7D7D7] font-Akaya_Kanadaka text-[18px] text-[#4F4F4F] focus-within:outline-none"
                  placeholder=""
                />
              </div>

           
              <div className="flex flex-col">
                <label
                  htmlFor="email"
                  className="font-Akaya_Kanadaka text-[18px] text-[#4F4F4F]"
                >
                  Email
                </label>
                <input
                  type="email"
                  name="email"
                  id="email"
                  className="border-b-[2px] border-[#D7D7D7] font-Akaya_Kanadaka text-[18px] text-[#4F4F4F] focus-within:outline-none"
                  placeholder=""
                />
              </div>

              
              <div className="flex flex-col">
                <label
                  htmlFor="message"
                  className="font-Akaya_Kanadaka text-[18px] text-[#4F4F4F]"
                >
                  Message
                </label>
                <textarea
                  name="message"
                  id="message"
                  className="border-b-[2px] border-[#D7D7D7] font-Akaya_Kanadaka text-[18px] text-[#4F4F4F] focus-within:outline-none"
                  placeholder=""
                />
              </div>

          
              <button className="uppercase font-Cabin font-semibold text-[16px] text-white bg-[#6246E4] px-[44px] py-5 rounded-[10px]">
                Send
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
